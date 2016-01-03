import sys
sys.path.append("api")
sys.path.append("util")

from flask import Flask, make_response, jsonify, request
import messages
import api

app = Flask(__name__)

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
@app.route("/api/v1.0/data/<int:notebook_id>/<int:visualization_id>", methods=['POST'])
def post_data(notebook_id, visualization_id):
    return api.post_data(notebook_id, visualization_id, request)

# method for getting data that has been pushed to vizserve.
@app.route("/api/v1.0/data/<int:notebook_id>/<int:visualization_id>", methods=['GET'])
def get_data(notebook_id, visualization_id):
    return api.get_data(notebook_id, visualization_id, request)

if __name__ == "__main__":
    app.run()
