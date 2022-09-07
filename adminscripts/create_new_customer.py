import pyodbc
from decouple import config

'''
Adds a new login for the Azure SQL Server 'c-connect'
'''

server = 'tcp:c-connect.database.windows.net'
database = 'master'
username = config('SERVER_ADMIN')
password = config('ADMIN_PASS')
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
customer_name = input("Enter name of new customer: ")
customer_pass = input("Enter strong password for new customer: ")
sqlcommand = "CREATE LOGIN "+customer_name+" WITH PASSWORD ='"+customer_pass+"';"
#cursor.execute("CREATE LOGIN ? WITH PASSWORD =?;",customer_name,customer_pass)
cursor.execute(sqlcommand)
cnxn.commit()

with open("credentials.txt", "w") as o:
    o.write(customer_name+"\n")
    o.write(customer_pass)
