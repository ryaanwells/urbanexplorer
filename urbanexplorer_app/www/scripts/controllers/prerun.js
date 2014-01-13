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
      $scope.stages = stages;
      return progress.getProgressions($scope.stages);
    }).then(function(progressions){
      var hasProgressForStage = true;
      var currentStage = $scope.stages[$scope.selected.startStage];
      var i;
      var aggDistance = 0;
      var completedDistance = 0;
      $scope.progressions = progressions;
      while (currentStage){
	aggDistance += currentStage.distance;
	if ($scope.progressions.hasOwnProperty(currentStage.id)
	    && hasProgressForStage){
	  completedDistance += $scope.progressions[currentStage.id].totalDistance;
	  aggDistance += currentStage.distance;
	  $scope.distanceUntilNextGoal = currentStage.distance - $scope.progressions[currentStage.id].totalDistance;
	}
	else {
	  hasProgressForStage = false;
	  $scope.distanceRemain += currentStage.distance;
	}
	console.log(currentStage.distance);
	currentStage = $scope.stages[currentStage.nextStage]; 
      }
      $scope.distanceRemain += $scope.distanceUntilNextGoal;
    });

});
