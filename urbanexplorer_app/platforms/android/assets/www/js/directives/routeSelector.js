UrbanExplorer.directive("routeSelector", function(routes, routePick, routesCompleted){
  'use strict';
  return {
    replace: true,
    restrict: 'E',
    templateUrl: 'html/directives/routeSelector.html',
    scope: {
      mission: '='
    },
    link: function($scope, $elem, $attrs){
      console.log("here");
      console.log($scope.mission);
      $scope.routes = [];
      $scope.show = false;

      $scope.routes = routes.getRoutesForMission($scope.mission.resource_uri);
      for (var i = 0; i < $scope.routes.length; i++){
	var routeCompleted = routesCompleted.getRC($scope.routes[i].resource_uri);
	if (routeCompleted){
	  $scope.routes[i].progress = routeCompleted.totalDistance;
	  $scope.routes[i].completed = routeCompleted.completed;
	  $scope.routes[i].percent = routeCompleted.totalDistance / $scope.routes[i].length * 100;
	}
	else {
	  $scope.routes[i].progress = 0;
	  $scope.routes[i].completed = false;
	  $scope.routes[i].percent = 0;
	}
      }

      $scope.toggle = function(){
	if ($scope.routes.length === 0){
	  $scope.routes = routes.getRoutesForMission($scope.mission.resource_uri);
	  if ($scope.routes.length > 0){
	    $scope.show = true;
	  }
	}
	else {
	  $scope.show = !$scope.show;
	}
      };

      $scope.select = function(route){
	routePick.set(route);
      };
    }
  };
});