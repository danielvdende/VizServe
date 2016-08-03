var notebookData = {};

window.onload = function(){
	var id = window.location.search.split("id=")[1];

	fetchNotebookInfo(id);

	fetchVisualizations(id);
}

function fetchNotebookInfo(id){
	var request = new XMLHttpRequest();
	request.open('GET', vizServeConfig.apiUrl + "/notebooks/" + id, true)
	request.onload = function() {
		if(request.status >= 200 && request.status < 400){
			notebookData.info = JSON.parse(request.responseText)
			console.log("HELLO", notebookData.info)
			var placeholders = document.querySelectorAll(".notebook_name");
			[].forEach.call(placeholders, function(placeholder){
				placeholder.innerHTML = notebookData.info.name;
			});
			document.title += notebookData.info.name;
		}
	}
	request.onerror = function() {
		errorHandler.networkError("notebook_error_panel", "Could not find info for this notebook")
	}
	try{
		request.send()
	} catch(e){
		errorHandler.networkError("notebook_error_panel", "Network error, could not establish connection to server");
	}
}

function fetchVisualizations(id){
	var request = new XMLHttpRequest();
	request.open('GET', vizServeConfig.apiUrl + "/notebooks/" + id + "/viz", true);

	request.onload = function() {
	  if (request.status >= 200 && request.status < 400) {
	    // Success!
	    notebookData.viz = JSON.parse(request.responseText);
	    renderViz()
	  } else {
	    // We reached our target server, but it returned an error
	    errorHandler.serverError("notebook_error_panel", "Could not fetch visualizations for this notebook from server.")
	  }
	};

	request.onerror = function() {
	  // There was a connection error of some sort
	  errorHandler.networkError("notebook_error_panel", "Network error, could not establish connection to server");
	  
	};
	try{
		request.send();
	} catch(e){
		errorHandler.networkError("notebook_error_panel", "Network error, could not establish connection to server");	
	}
}

function renderViz(){
	var fragment = document.createDocumentFragment();
	var row;
	var iframe;
	for(var i = 0; i < notebookData.viz.length; i++){
		row = document.createElement("div");
		row.className = "row";
		iframe = document.createElement("iframe")
		iframe.src = "modules/" + notebookData.viz[i].type + ".html?id=" + notebookData.viz[i]._id;
		iframe.name = "john";
		iframe.id = notebookData.viz[i]._id + "_frame";
		row.appendChild(iframe);
		fragment.appendChild(row);
	}
	document.getElementById("viz_container").appendChild(fragment);
}