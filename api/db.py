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
    print "sometvizservehing"

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

# TODO: rework, possibly unnecessary to include notebook_id
def write_data(notebook_id, visualization_id, data):
    return db.vizserve.insert_one({"notebook_id":notebook_id, "visualization_id":visualization_id,"data":data})

def get_notebooks():
    return list(db.notebooks.find({}, {"_id":1, "name":1,}))

def get_visualizations_for_notebook(notebook_id):
    # first get a list of viz_ids that require fetching.
    viz_ids = list(db.notebooks.find({"_id":notebook_id}, {"viz":1, "_id":0}))
    viz_ids = viz_ids[0]['viz']
    # now fetch the names and id's of these visualizations
    return list(db.viz.find({"_id":{"$in":viz_ids}}, {"_id":1, "name":1, "type":1}))

def create_notebook(notebook):
    # print notebook
    print "hello"
    print notebook
    res = db.notebooks.insert(notebook)
    print res

initialize()

# create_notebook({"_id":"testy", "name":"HI"})