import json
import db
import uuid


def post_data(visualization_id, request):
    """Post new data for an existing visualization (i.e. add data to existing
    object in db).

    Arguments:
    visualization_id -- id of the visualization for which the data posted is.
    request          -- Flask request object, with the data for the 
                        visualization in the json field.
    """
    data = request.json
    result = db.write_viz_data(visualization_id, data)
    # TODO: return proper value to describe succes/failure of data write.
    return {"empty": result}


def post_data_new_viz(request):
    """Post new data for a new visualization (i.e. we don't know the id, so 
    create some new visualization object to hold this data). The method should
    return the _id of the visualization created.

    Arguments:
    request --  Flask request object, with the data for the visualization
                in the json field.
    """
    # check if any name has been provided for the visualization, otherwise 
    # generate a random one.
    data = request.get_json()
    print type(data)
    print data
    if not 'name' in data:
        data.name = uuid.uuid4()

    # generate the viz id.
    data['_id'] = uuid.uuid4().hex

    # write the new object to db.
    result = db.write_viz_data(data['_id'], data)
    return result


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
    """Create a new notebook given a notebook object. This object should
    have keys: '_id' and 'name', otherwise an error will be returned.

    Arguments:
    notebook -- dictionary containing info for the notebook (should contain
                _id and name as keys.
    """
    if "_id" in notebook and "name" in notebook:
        db.create_notebook(notebook)
        return "Notebook created"
    else:
        return "Invalid notebook"


def remove_visualization(visualization_id):
    """ TODO: comment
        TODO: return sensible value
    """
    db.remove_visualization(visualization_id)
    return {"Removed": visualization_id}


def remove_notebook(notebook_id):
    """ TODO: comment
        TODO: return sensible value
    """
    db.remove_notebook(notebook_id)
    return {"Removed": notebook_id}


def update_notebook(notebook_id, data):
    """ TODO: comment
        TODO: return sensible value
        TODO: should also have a method that allows updating of specific fields instead of full overwrite.
    """
