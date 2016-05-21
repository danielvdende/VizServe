document.getElementById("menu-toggle").addEventListener("click", function(e){
    e.preventDefault();
    document.getElementById("wrapper").classList.toggle("toggled");
});

var vizServeConfig = {
  "apiUrl": "http://localhost:5000/api/v1.0",
  "notebookHashLength": 20
}

var errorHandler = {
	serverError: function(parentElementID, message){
		var error_panel = document.getElementById(parentElementID);
		error_panel.classList.remove("hidden");
		error_panel.innerHTML = "<strong>SERVER_ERROR</strong> <br />" + message;
		setTimeout(function(){error_panel.classList.add("hidden");}, 5000);
	},

	userError: function(parentElementID, message){
		var error_panel = document.getElementById(parentElementID);
		error_panel.classList.remove("hidden");
		error_panel.innerHTML = message;
		setTimeout(function(){error_panel.classList.add("hidden");}, 5000);
	},

	networkError: function(parentElementID, message){
		var error_panel = document.getElementById(parentElementID);
		error_panel.classList.remove("hidden");
		error_panel.innerHTML = "<strong>NETWORK_ERROR</strong> <br />" + message;

		// network errors should always be displayed to prevent confusion. (i.e. error disappearing doesn't mean network is ok again).
	}

}
