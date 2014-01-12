UrbanExplorer.controller("PrerunCtrl", function($scope, routePick, $http, $q, stages, progress){
  "use strict";
  $scope.selected = routePick.get();
  
  $scope.stages = {};
  $scope.progressions = [];
  
  $scope.distanceRemain = 0;
  $scope.distanceUntilNextGoal = 0;
  
  stages.getStages($scope.selected.stages)
    .then(function(stages){
      console.log("resolved")
	for (var i in stages){
	  console.log(stages[i].name)
	};

	$scope.stages = stages;
	return progress.getProgressions($scope.stages);
      
    }).then(function(progressions){
      var hasProgressForStage = true;
      var currentStage = $scope.selected.startStage;
      var i;
      var totalDistance = 0;
      var completedDistance = 0;
      $scope.progressions = progressions;
      // while (currentStage){
	// totalDistance += currentStage.distance;
	// if ($scope.progressions.hasOwnProperty(currentStage.id)){
	  // completedDistance += $scope.progressions
	// }
      // }
    });
});
