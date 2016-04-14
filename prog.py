import os

from flask import Flask

from flask import request

import pymongo

import json

from bson import json_util

from bson import objectid

import re

app = Flask(__name__)

@app.route('/')

def employees():

 #setup the connection

 conn = pymongo.Connection(os.environ['OPENSHIFT_MONGODB_DB_URL'])

 db = conn.myapp

 #query the DB for all the employee

 result = db.employee.find()

 #Now turn the results into valid JSON

 return 

str(json.dumps({'results':list(result)},default=json_util.default))

if __name__ == '__main__':

 app.run()
