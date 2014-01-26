UrbanExplorer.directive("routeSelector", function(routes, routePick){
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
