import os
import pymongo
import json

# TODO: for all these methods, we should add some kind of error handling for 
# the database calls. Unclear what happens now if the call fails.

config = {}
client = {}
db = {}
credentials = {}
file_loc = os.path.dirname(__file__)


def initialize():
    # need to make variables global here in order to be allowed to reassign value.
    global config, client, db, credentials

    # first open the configuration file and load the settings
    with open(os.path.join(file_loc, '../conf/db.json')) as data_file:
        config = json.load(data_file)

        # TODO: use credentials for database connection
        # with open(os.path.join(file_loc, '../credentials/db.json')) as cred_file:
        #     credentials = json.load(cred_file)

        # now initialize a client object for the db connection
        client = pymongo.MongoClient()
        db = client[config["database"]]


def write_viz_data(visualization_id, data):
    # TODO: possibly add validation for visualization_id
    db.viz.update(
        {"_id": visualization_id},
        data,
        upsert=True
    )
    return "Wrote viz data for {}".format(visualization_id)


def get_notebooks():
    """Return a the ids and names of all existing notebooks.
    """
    return list(db.notebooks.find({}, {"_id": 1, "name": 1}))


def get_visualizations_for_notebook(notebook_id):
    # first get a list of viz_ids that require fetching.
    viz_ids = list(db.notebooks.find({"_id": notebook_id}, {"viz": 1, "_id": 0}))

    if(viz_ids[0] == {}):
        # if there are no visualizations for this notebook, just return an empty list.
        return list()

    viz_ids = viz_ids[0]['viz']
    # now fetch the names and id's of these visualizations
    return list(db.viz.find({"_id": {"$in": viz_ids}}, {"_id": 1, "name": 1, "type": 1}))


def create_notebook(notebook):
    print type(notebook)
    print notebook
    res = db.notebooks.insert(notebook)
    # TODO: add som return value to indicate whether the insertion completed.


def get_visualization(visualization_id):
    return db.viz.find_one({"_id": visualization_id})


def remove_visualization(visualization_id):
    return db.viz.remove({"_id": visualization_id})


def remove_notebook(notebook_id):
    return db.notebooks.remove({"_id": notebook_id})


def update_notebook(notebook_id, data):
    return db.notebooks.update(
        {'_id': notebook_id},
        data,
        upsert=True
    )


def incremental_update_notebook(notebook_id, data):
    pass

def get_notebook_info(notebook_id):
    return list(db.notebooks.find(
        {'_id':notebook_id},
        {'viz':0}
        ))[0]


initialize()
