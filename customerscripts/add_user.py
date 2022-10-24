import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import login
import connection
import bcrypt
 
username = input("\nEnter username: ")
passw = input("\nEnter password: ")
salt = bcrypt.gensalt() #generate salt
passw = login.hash(passw.encode('utf-8')+salt) #hash password along with the salt 

sqlcommand = '''
INSERT INTO login VALUES(?,?,?);
'''
connection.cursor.execute(sqlcommand,username,passw,salt)
connection.cnxn.commit()

sqlcommand = '''
INSERT INTO udetails VALUES(?,?,?,?,?,?);
'''

name = input("Enter name: ")
dob = input("Enter DOB (YYYY/MM/DD): ")
branch = input("Enter branch: ")
year = int(input("Enter year of study: "))
u_type = input("Enter user type: ")

connection.cursor.execute(sqlcommand,username,name,dob,branch,year,u_type)
connection.cnxn.commit()