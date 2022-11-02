import pyodbc
from decouple import config

server = 'tcp:c-connect-login.database.windows.net'
database = input("Enter the name of the database: ")
username = config('SERVER_ADMIN')
password = config('ADMIN_PASS')
with open("credentials.txt", "r") as o:
    customer_name = o.readline()
    customer_pass = o.readline()
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
sqlcommand = "CREATE USER "+customer_name+" FROM LOGIN "+customer_name+" WITH DEFAULT_SCHEMA=dbo;"
cursor.execute(sqlcommand)
cnxn.commit()

#cursor.execute("CREATE LOGIN ? WITH PASSWORD =?;",customer_name,customer_pass)
sqlcommand = "ALTER ROLE db_owner ADD MEMBER "+customer_name+";"
cursor.execute(sqlcommand)
cnxn.commit()