import json
import db

def post_data(notebook_id, visualization_id, request):
    print "post to", notebook_id, visualization_id, request
    data = request.json
    return {"empty": "message"}


def get_data(notebook_id, visualization_id, request):
    print "get to", notebook_id, visualization_id, request
    db.test_method()
    return {"empty":"message"}
