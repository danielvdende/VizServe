var notebookData = {};

window.onload = function(){
	var id = window.location.search.split("id=")[1];

	fetchVisualizations(id);
}

function fetchVisualizations(id){
	var request = new XMLHttpRequest();
	request.open('GET', vizServeConfig.apiUrl + "/notebooks/" + id, true);

	request.onload = function() {
	  if (request.status >= 200 && request.status < 400) {
	    // Success!
	    notebookData.viz = JSON.parse(request.responseText);
	    renderViz()
	  } else {
	    // We reached our target server, but it returned an error
	    // TODO: proper error handling
	    console.log("ohnoes");
	  }
	};

	request.onerror = function() {
	  // There was a connection error of some sort
	  // TODO: proper error handling
	  console.log("different ohnoes");
	};

	request.send();
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
		row.appendChild(iframe);
		fragment.appendChild(row);
	}
	document.getElementById("viz_container").appendChild(fragment);
}