UrbanExplorer.directive("achievementView", function(routes, stages, progress){
  "use strict";
  return {
    templateUrl: "html/directives/achievementView.html",
    replace: true,
    restrict: 'E',
    scope: {
      mission: '='
    },
    link: function($scope, $elem, $attrs){
      $scope.open = false;
      $scope.routes = routes.getRoutesForMission($scope.mission.resource_uri);
      angular.forEach($scope.routes, function(route){
	angular.forEach(route.stages, function(stage){
	  progress.getProgressions([stage], true)
	    .then(function(progressions){
	      angular.forEach(progressions, function(prog){
		if (prog.completed){
		  console.log("completed");
		  stage.completed = true;
		  return;
		}
	      });
	    });
	});
      });
      $scope.toggle = function(){
	$scope.open = !$scope.open;
      }
    }
  };
});
