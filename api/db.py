# import pymongo
import json

config = {}
client = {}
db = {}

# get the data for a given visualization in a given notebook
def get_data(notebook_id, visualization_id):
    print "something"

def initialize():
    # need to make variables global here in order to be allowed to reassign value.
    global config, client, db

    # first open the configuration file and load the settings
    with open('conf/db.json') as data_file:
        config = json.load(data_file)


    # now initialize a client object for the db connection
	# client = pymongo.MongoClient()
	# db = client[config["database"]]

initialize()
