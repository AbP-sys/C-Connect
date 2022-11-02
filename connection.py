import pyodbc
from cassandra.cluster import Cluster

# these credentials are for development only. No sensitive data stored in the database.
server = 'tcp:c-connect-login.database.windows.net'
database = 'test-uni'
username = 'TestUniAdmin'
password = 'SVDSkvvkjk45'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


cluster = Cluster()
session = cluster.connect()
