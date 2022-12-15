"""
This file is to be deployed on azure as a web app or a remote server running cassandra locally
"""

from flask import Flask,request
from cassandra.cluster import Cluster

app = Flask(__name__)

@app.route('/')
def index():
   	return render_template('index.html')

@app.route('/mails/', methods=['GET'])
def get_mails():
    cluster = Cluster()
    session = cluster.connect()
    args = request.args
    domain = args.get('domain')
    dept = args.get('dept')
    result = session.execute("SELECT subject,body,sender FROM testuni.mails WHERE domain='{}' AND dept='{}' ALLOW FILTERING".format(domain,dept))
    mails=[]
    for x in range(len(result.current_rows)):
	    mails.append(result[x])
    return mails

if __name__ == '__main__':
	app.run(debug=True)
