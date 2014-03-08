UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location, self, routes, missions, $http, routesCompleted, routePick) {
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

  self.getSelf().then(function(response){
    $scope.self = response;
  }, function(response){
    $scope.self = response;
  });

  routes.getRoutes().then(function(routes){
    routePick.set(routes[0]);
  });
  routesCompleted.getCompleted();
  

});

