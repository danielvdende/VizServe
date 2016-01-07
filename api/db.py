# import pymongo
import json
import psycopg2

config = {}
client = {}
db = {}
credentials = {}

# get the data for a given visualization in a given notebook
def get_data(notebook_id, visualization_id):
    print "something"

def initialize():
    # need to make variables global here in order to be allowed to reassign value.
    global config, client, db, credentials

    # first open the configuration file and load the settings
    with open('../conf/db.json') as data_file:
        config = json.load(data_file)

    with open('../credentials/db.json') as cred_file:
        credentials = json.load(cred_file)

    # now initialize a client object for the db connection
	# client = pymongo.MongoClient()
	# db = client[config["database"]]



    try:
        conn = psycopg2.connect(
            "dbname=" + config["database"] +
            " user=" + credentials["user"] +
            " host=" + config["host"] +
            " password=" + credentials["password"])
    except:
        print "I am unable to connect to the database"

initialize()
