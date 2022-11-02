import random
import connection as cassandra
#selection = random.randint(1,4)
userselection = { 1:"general",2:"placement",3:"exam",4:"other"}

def display(user,selection):
    """
    fetches notices from the server based on selection
    """

    print("Viewing:" + userselection[selection])

    result = cassandra.session.execute("SELECT * FROM testuni.mails WHERE domain='{}' AND dept='{}' ALLOW FILTERING".format(userselection[selection],user.branch))
    return result


def LinkClick(user,mailid):
    """
    Updates 'seen' list of a particular mail
    """
    query = cassandra.session.prepare("UPDATE mails SET seen = seen + {'"+user.email+"'} WHERE mailid = ? ")
    cassandra.session.execute(query,{mailid})
    print("seen")
