# VizServe
VizServe is a simple, REST-based visualization server, which makes it really easy to quickly get insight into your data through visualizations. VizServe aims to support both static and streaming data, and aims to be easily extendable with new visualizations. A database supports VizServe in order to provide persistency. At the moment, this database is PostgreSQL, but the modular design makes it relatively painless to switch to a different database of your choice.

## Installation

## Dependencies
- pip
- flask
- Socketio
- flask-socketio
- flask-cors

## API
VizServe's API offers RESTful endpoints for both the storage and retrieval of data. The API has the following routes:
#### GET 		/api/v1.0/viz/{visualization_id}
Get all data associated with a given visualization_id
#### PUT 		/api/v1.0/viz/{visualization_id}
Update an existing visualization configuration (e.g. axis config, color config, etc.)
#### DELETE 	/api/v1.0/viz/{visualization_id}
Delete a given visualization. This will also remove any data associated with this visualization, so be careful!
#### GET 		/api/v1.0/notebooks
Get a list of all notebooks.
#### GET 		/api/v1.0/notebooks/{notebook_id}
Get a list of visualizations associated with a given notebook_id. Should also return other information regarding the notebook.
#### PUT 		/api/v1.0/notebooks/{notebook_id}
Update an existing notebook (e.g. notebook configuration, name, viz ids, etc.)
NOTE: at the moment this is an overwriting update (i.e. the entire config is overwritten,
if you want to keep any existing config, this needs to be supplied in the request)
#### DELETE 	/api/v1.0/notebooks/{notebook_id}
Remove a given notebook. This will NOT remove the visualizations that were created within. Rather, it should be possible to retrieve existing visualizations in the frontend.
#### POST 		/api/v1.0/notebooks
Create a new notebook.
#### PUT 		/api/v1.0/data/{visualization_id}
Send new data for an existing visualization with a given id. 
#### POST 		/api/v1.0/data
If no visualization_id is provided, the same logic as the PUT route is followed, but a visualization object is created, and the id generated is returned for further reference.

## Example

## Vagrant box

## Future additions
Currently, VizServe is very much in development. The functionality described in the above is not yet available in this repository. In this section a list of additions in the future will be shown, so that users have some idea of the future roadmap:
- Both PostgreSQL and MongoDB connection scripts.
- Vagrant box to quickly deploy a VizServe server.
- install script
