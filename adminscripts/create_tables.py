import pyodbc
from decouple import config

server = 'tcp:c-connect-login.database.windows.net'
database = 'test-uni'
with open("credentials.txt", "r") as o:
    username = o.readline()
    password = o.readline()
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
sqlcommand = '''
CREATE TABLE login(
    username VARCHAR(30) PRIMARY KEY,
    pass VARCHAR(64) NOT NULL,
    salt VARCHAR(29) NOT NULL
    );
'''
cursor.execute(sqlcommand)
cnxn.commit()
cursor.execute('''
CREATE TABLE udetails(
    uid VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    DOB DATE,
    branch VARCHAR(20),
    year INT CHECK (year IN (1,2,3,4,5)),
    type VARCHAR(20),
    FOREIGN KEY (uid) REFERENCES login(username)
);
''')
cnxn.commit()