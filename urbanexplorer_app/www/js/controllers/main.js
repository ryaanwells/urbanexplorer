UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location, self, routes, missions, $http, routesCompleted, routePick, achievements) {
  'use strict';
  $scope.coords = [];

  // geolocation.watchPosition();
  
  $scope.self = {
    totalDistance: 0,
    time: {
      hours: 0,
      minutes: 0,
      seconds: 0
    }
  }

  $scope.ach = {
    G: 0,
    S: 0,
    B: 0
  }

  self.getSelf().then(function(response){
    $scope.self = response;
    console.log(response.totalTime);
    if (!response.totalTime || response.totalTime === 0){
      response.totalTime = 1;
    }
    $scope.avgSpeed = response.totalDistance / Math.floor(response.totalTime / 1000);
    console.log($scope.avgSpeed);
    $scope.avgSpeed = $scope.avgSpeed.toFixed(1);
  }, function(response){
    $scope.self = response;
  });
  
  achievements.get().then(function(allAch){
    var ach = allAch[0];
    angular.forEach(ach, function(a){
      if (a.completed){
	console.log(a.id);
	$scope.ach[a.value]++;
      }
    });
    $scope.ach["S"] -= $scope.ach["G"];
    $scope.ach["B"] -= $scope.ach["G"] + $scope.ach["S"];
  });
  
  routes.getRoutes()
  // .then(function(routes){
  //   routePick.set(routes[0]);
  // });
  routesCompleted.getCompleted();
  
  
});

