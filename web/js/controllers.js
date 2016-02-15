var vizServeControllers = angular.module("vizServeControllers", []);

vizServeControllers.controller("HomePageCtrl", ["$scope", "$http",
  function($scope, $http){
    $http.get("http://localhost:5000/api/v1.0/notebooks").then(function(response){
      console.log(response);
    });
  }
])
