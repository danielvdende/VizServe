document.getElementById("menu-toggle").addEventListener("click", function(e){
    e.preventDefault();
    document.getElementById("wrapper").classList.toggle("toggled");
});

var vizServeConfig = {
  "apiUrl": "http://localhost:5000/api/v1.0"
}
