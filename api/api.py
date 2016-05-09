import json
import db

def post_data(notebook_id, visualization_id, request):
    print "post to", notebook_id, visualization_id, request
    data = request.json
    result = db.write_data(notebook_id, visualization_id, data)
    print result
    return {"empty": result}


def get_data(visualization_id, request):
    print "get to", visualization_id, request
    visualization = db.get_visualization(visualization_id)
    return visualization

def get_notebooks():
    notebooks = db.get_notebooks()
    return notebooks

def get_visualizations_for_notebook(notebook_id):
    visualizations = db.get_visualizations_for_notebook(notebook_id)
    return visualizations

def create_notebook(notebook):
    print "api " + notebook
    # # first validate the notebook.
    if "_id" in notebook and "name" in notebook:
        db.create_notebook(notebook)
        return "Notebook created"
    else:
        return "Invalid notebook"