import connection
from hashlib import sha256

class userDetails:
    def __init__(self,email, name, DOB, branch, year,type):
        self.email = email
        self.name = name
        self.DOB = DOB
        self.branch = branch
        self.year = year
        self.type = type

def fetchdetails(uid):
    """
    fetches user details from the database and returns user object with
     all the attributes
    """
    connection.cursor.execute("SELECT * FROM udetails WHERE uid=?;",uid)
    row = connection.cursor.fetchone()
    return userDetails(row[0],row[1],row[2],row[3],row[4],row[5])

def authentication(user, pwd):
    """
    Runs a query against the database to very credentials
    """
    connection.cursor.execute("SELECT COUNT(username) FROM login WHERE username=?;",user)
    row = connection.cursor.fetchone()
    if(row[0] == 1):
        connection.cursor.execute("SELECT pass FROM login WHERE username=?;",user)
        row = connection.cursor.fetchone()
        if(row[0] == pwd):
            print("login successful")
            return 0
        else:
            #raise ValueError("incorrect password")
            return -1
    else:
        #raise ValueError("user not registered")
        return -1

def hash(pwd):
    hashobj = sha256()
    hashobj.update(pwd.encode('utf-8'))
    hash = hashobj.hexdigest()
    return hash
