import sys
sys.path.append("api")
sys.path.append("util")

from flask import Flask, make_response, jsonify, request
from flask.ext.cors import CORS
import messages
import api
import json

app = Flask(__name__)
CORS(app)
# GENERAL
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(messages.notFound))

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify(messages.badRequest))

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify(messages.serverError))

# API
# method for posting data from an arbitrary application to VizServe
# this route assumes both notebook_id and visualization_id are available.
@app.route("/api/v1.0/data/<notebook_id>/<visualization_id>", methods=['POST'])
def post_data(notebook_id, visualization_id):
    return make_response(jsonify(api.post_data(notebook_id, visualization_id, request)))

# method for getting data that has been pushed to vizserve.
@app.route("/api/v1.0/data/<int:notebook_id>/<int:visualization_id>", methods=['GET'])
def get_data(notebook_id, visualization_id):
    return make_response(jsonify(api.get_data(notebook_id, visualization_id, request))).inserted_id

@app.route("/api/v1.0/notebooks", methods=['GET'])
def get_notebooks():
	return make_response(json.dumps(api.get_notebooks()))

# returns a list of visualization ids (+ their type) to be used as parameters for various iframes
@app.route("/api/v1.0/notebooks/<notebook_id>", methods=['GET'])
def get_visualizations_for_notebook(notebook_id):
	return make_response(json.dumps(api.get_visualizations_for_notebook(notebook_id)))

@app.route("/api/v1.0/notebooks", methods=['POST'])
def create_notebook():
	print "HI"
	return make_response(api.create_notebook(json.dumps(request.get_json())))

if __name__ == "__main__":
    with open('conf/server.json') as data_file:
        config = json.load(data_file)
    app.run(host=config["host"], port=config["port"])
