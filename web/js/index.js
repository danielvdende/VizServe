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
	    console.log("ohnoes");
	  }
	};

	request.onerror = function() {
	  // There was a connection error of some sort
	  console.log("different ohnoes");
	};

	request.send();
}

function renderNotebooks(){
	var fragment = document.createDocumentFragment();
	var element;
	for(var i=0; i < indexData.notebooks.length; i++){
		console.log(indexData.notebooks[i]);
		element = document.createElement("a");
		element.className = "list-group-item";
		element.innerHTML = "Notebook " + indexData.notebooks[i].notebook_id;
		element.href = indexData.notebooks[i];
		fragment.appendChild(element);
	}
	document.getElementById("notebook_list").appendChild(fragment);
}