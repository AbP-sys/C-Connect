import pyodbc
from cassandra.cluster import Cluster

server = 'localhost'
database = 'CCdB'
username = 'sa'
password = 'lqsS1.86PROton'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


cluster = Cluster()
session = cluster.connect('mailhouse')
