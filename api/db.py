import os
import pymongo
import json

config = {}
client = {}
db = {}
credentials = {}
file_loc = os.path.dirname(__file__)

# get the data for a given visualization in a given notebook
def get_data(notebook_id, visualization_id):
    print "something"

def initialize():

    # need to make variables global here in order to be allowed to reassign value.
    global config, client, db, credentials

    # first open the configuration file and load the settings
    with open(os.path.join(file_loc, '../conf/db.json')) as data_file:
        config = json.load(data_file)

    with open(os.path.join(file_loc, '../credentials/db.json')) as cred_file:
        credentials = json.load(cred_file)

    # now initialize a client object for the db connection
	client = pymongo.MongoClient()
	db = client[config["database"]]

def write_data(notebook_id, visualization_id, data):
    return db.vizserve.insert_one({"notebook_id":notebook_id, "visualization_id":visualization_id,"data":data})

def get_notebooks():
    return list(db.vizserve.find({}, {"notebook_id":1, "notebook_name":1, "_id":0}))

initialize()