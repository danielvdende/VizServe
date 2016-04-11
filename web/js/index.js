var indexData = {};

window.onload = function(){
	fetchNotebooks();
}

function fetchNotebooks(){
	var request = new XMLHttpRequest();
	request.open('GET', vizServeConfig.apiUrl + "/notebooks", true);

	request.onload = function() {
	  if (request.status >= 200 && request.status < 400) {
	    // Success!
	    indexData.notebooks = JSON.parse(request.responseText);
	    renderNotebooks()
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

function renderNotebooks(){
	var fragment = document.createDocumentFragment();
	var element;
	for(var i=0; i < indexData.notebooks.length; i++){
		element = document.createElement("a");
		element.className = "list-group-item";
		element.innerHTML = "Notebook " + indexData.notebooks[i]._id;
		element.href = "notebook.html?id=" + indexData.notebooks[i]._id;
		fragment.appendChild(element);
	}
	document.getElementById("notebook_list").appendChild(fragment);
}

function createNotebook(notebookName){
	// first generate a random hash that should serve as id.
	var notebook = {
		"_id": generateId(vizServeConfig.notebookHashLength),
		"name": notebookName
	}

	// send new notebook to the server
	var request = new XMLHttpRequest();
	request.open('POST', vizServeConfig.apiUrl + "/notebooks", true);
	request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

	request.onload = function() {
	  	if (request.status >= 200 && request.status < 400) {
	    	// Success!
			console.log(request)
		} else {
	    	// We reached our target server, but it returned an errors
	    	// TODO: proper error handling
	    	console.log("ohnoes");
	  	}
	};

	request.onerror = function() {
	  // There was a connection error of some sort
	  // TODO: proper error handling
	  console.log("different ohnoes");
	};

	request.send(JSON.stringify(notebook));

	// only if successful add the notebook as a link to the dashboard.
}

function generateId(n) {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < n; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}

document.getElementById("add_notebook_btn").addEventListener("click", function(){
	var notebookName = prompt("Please enter a name for the new notebook");
	if(notebookName === null || notebookName === ""){
		alert("Notebook not created, invalid notebook name provided");
	} else {
		createNotebook(notebookName);
	}
});