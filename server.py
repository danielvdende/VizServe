import sys

sys.path.append("api")
sys.path.append("util")

from flask import Flask, make_response, request
from flask.ext.cors import CORS
import messages
import api
import json

app = Flask(__name__)
CORS(app)


# GENERAL
@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps(messages.notFound))


@app.errorhandler(400)
def bad_request(error):
    return make_response(json.dumps(messages.badRequest))


@app.errorhandler(500)
def server_error(error):
    return make_response(json.dumps(messages.serverError))


# API

# method for getting data that has been pushed to vizserve.
@app.route("/api/v1.0/viz/<visualization_id>", methods=['GET'])
def get_data(visualization_id):
    return make_response(json.dumps(api.get_data(visualization_id, request)))


# Update an existing visualization configuration
# TODO: determine endpoint signature in terms of parameters/payload.
# TODO: implement method.
@app.route("/api/v1.0/viz/<visualization_id>", methods=['PUT'])
def update_visualization(visualization_id):
    return None


# Remove a given visualization (should also remove any data associated with
# this visualization)
@app.route("/api/v1.0/viz/<visualization_id>", methods=['DELETE'])
def remove_visualization(visualization_id):
    return make_response(json.dumps(api.remove_visualization(visualization_id)))


# returns a list of notebook objects with _id and name per notebook.
@app.route("/api/v1.0/notebooks", methods=['GET'])
def get_notebooks():
    return make_response(json.dumps(api.get_notebooks()))


@app.route("/api/v1.0/notebooks/<notebook_id>", methods=['GET'])
def get_notebook_info(notebook_id):
    return make_response(json.dumps(api.get_notebook_info(notebook_id)))

# returns a list of visualization ids (+ their type) associated with a given notebook
@app.route("/api/v1.0/notebooks/<notebook_id>/viz", methods=['GET'])
def get_visualizations_for_notebook(notebook_id):
    return make_response(
        json.dumps(api.get_visualizations_for_notebook(notebook_id)))


# Update an existing notebook (e.g. notebook config)
# TODO: determine endpoint signature (params/payload)
# TODO: implement method
@app.route("/api/v1.0/notebooks/<notebook_id>", methods=['PUT'])
def update_notebook(notebook_id):
    return make_response(json.dumps(api.update_notebook(notebook_id, request.get_json())))


# Remove a given notebook. This will NOT remove the visualizations created
# within
@app.route("/api/v1.0/notebooks/<notebook_id>", methods=['DELETE'])
def remove_notebook(notebook_id):
    return make_response(json.dumps(api.remove_notebook(notebook_id)))


# Create a new notebook.
@app.route("/api/v1.0/notebooks", methods=['POST'])
def create_notebook():
    return make_response(api.create_notebook(request.get_json()))


# Post data to an existing visualization (i.e. for which the viz id is known
# and supplied)
@app.route("/api/v1.0/data/<visualization_id>", methods=['PUT'])
def put_data(visualization_id):
    return make_response(json.dumps(api.post_data(visualization_id, request)))


# Post data without any identification of the visualization. This should
# result in the creation of a new visualization, whose details should be 
# returned to the user.
@app.route("/api/v1.0/data", methods=['POST'])
def post_data_new_viz():
    return make_response(api.post_data_new_viz(request))


if __name__ == "__main__":
    with open('conf/server.json') as data_file:
        config = json.load(data_file)
    app.run(host=config["host"], port=config["port"], debug=True)
