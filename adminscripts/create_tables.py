import pyodbc
from decouple import config

server = 'tcp:c-connect.database.windows.net'
database = 'test-uni'
with open("credentials.txt", "r") as o:
    username = o.readline()
    password = o.readline()
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
sqlcommand = '''
CREATE TABLE login(
    username VARCHAR(30) PRIMARY KEY,
    pass VARCHAR(50) NOT NULL
    );
'''
cursor.execute(sqlcommand)
cnxn.commit()
cursor.execute('''
CREATE TABLE udetails(
    email VARCHAR(30) PRIMARY KEY,
    name VARCHAR(30),
    DOB DATE,
    branch VARCHAR(20),
    year INT CHECK (year IN (1,2,3,4,5)),
    type VARCHAR(20),
    FOREIGN KEY (email) REFERENCES login(username)
);
''')
cnxn.commit()