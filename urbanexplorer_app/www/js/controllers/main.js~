UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location, self, routes, missions, $http) {
  'use strict';
  $scope.coords = [];

  //geolocation.pollPosition();
  
  $scope.self = "";

  $scope.running = false;

  self.getSelf().then(function(response){
    $scope.self = response;
  }, function(response){
    $scope.self = response;
  });

  routes.getRoutes();
  
  $scope.swipeLeft = function(){
    $location.path("/targets/");
  };
  
  $scope.swipeRight = function(){
    $location.path("/achievements/");
  };
  
  $scope.startSession = function(route){
    $scope.running = true;
    
    console.log(route.resource_uri);
    console.log($scope.self.resource_uri);

    var progressConfig = {
      method: "POST",
      url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/progress/",
      data: {
	stageID: route.resource_uri,
	userID: $scope.self.resource_uri
      }
    }

    var sessionConfig = {
      method: "POST",
      url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/session/",
      data: {
	userID: $scope.self.resource_uri
      }
    }

    $http(progressConfig).then(function(success){
      console.log(success.data.resource_uri);
      geolocation.getCurrentPosition()
	.then(function(location){
	  console.log(success.data.resource_uri);
	  console.log(location.coords.latitude);
	  console.log(location.coords.longitude);
	  sessionConfig.data.currentProgress = success.data.resource_uri;
	  sessionConfig.data.allProgress = [success.data.resource_uri];
	  sessionConfig.data.lastLon = location.coords.latitude;
	  sessionConfig.data.lastLat = location.coords.longitude;
	  return $http(sessionConfig);
	}, function(failure){
	  console.log(failure);
	}).then(function(success){
	  console.log(success);
	}, function(failure){
	  console.log(failure);
	  console.log(failure.error_message);
	});
    }, function(failure){
      for (var a in failure){
	if (failure.hasOwnProperty(a)){
	  console.log(failure[a]);
	}
      }
      console.log(failure.error_message);
    }); 
  }
  
  /*
    $scope.$watch(
    function(){
    return geolocation.getCoordinatesList();
    }, 
    function(newList, oldList){
    console.log(newList);
    $scope.coords = newList;
    },
    true
    );
  */

});

