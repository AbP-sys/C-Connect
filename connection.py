import pyodbc
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from ssl import PROTOCOL_TLSv1_2, CERT_REQUIRED, SSLContext, CERT_NONE

def establish_connection():
    #mssql server
    # these credentials are for development only. No sensitive data stored in the database.
    server = 'tcp:c-connect-login.database.windows.net'
    database = 'test-uni'
    username = 'TestUniAdmin'
    password = 'SVDSkvvkjk45'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    global cursor
    cursor = cnxn.cursor()

    #cassandra cluster
    ssl_context = SSLContext(PROTOCOL_TLSv1_2)
    ssl_context.verify_mode = CERT_NONE
    auth_provider = PlainTextAuthProvider(username='c-connect', password='rTL5XH7vHOeIvk4UL5R39WHwFf2RCzdrp8Poon16O8rFaUgpS2na0SHcRJpy8yS83S1ab2nEQT0xQul7bjpriQ==')
    #cluster = Cluster(['c-connect.cassandra.cosmos.azure.com'], port = '10350', auth_provider=auth_provider,ssl_context=ssl_context)
    cluster = Cluster()
    global session
    session = cluster.connect()

