import connection
from hashlib import sha256

class userDetails:
    def __init__(self, name, DOB, branch, year,type):
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
    return userDetails(row[0],row[1],row[2],row[3],row[4])

def authentication(user, ent_pwd):
    """
    Runs a query against the database to very credentials
    """
    connection.establish_connection()
    connection.cursor.execute("SELECT COUNT(username) FROM login WHERE username=?;",user)
    row = connection.cursor.fetchone()
    if(row[0] == 1):
        connection.cursor.execute("SELECT salt FROM login WHERE username=?;",user) 
        salt = connection.cursor.fetchone()[0] #fetch salt
        ent_pwd = hash(ent_pwd.encode('utf-8')+salt.encode('utf-8')) #append salt to the entered password and hash it 
        connection.cursor.execute("SELECT pass FROM login WHERE username=?;",user)
        true_pwd = connection.cursor.fetchone()[0]
        if(true_pwd == ent_pwd): #compare computed hash with the hash stored in dB
            print("login successful")
            return 0
        else:
            #raise ValueError("incorrect password")
            return -1
    else:
        #raise ValueError("user not registered")
        return -1

def hash(pwd):
    """
    returns 64 characters long hashed alphanumeric string 
    """
    hashobj = sha256()
    hashobj.update(pwd)
    hash = hashobj.hexdigest()
    return hash
