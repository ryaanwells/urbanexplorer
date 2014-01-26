UrbanExplorer.controller('PrerunCtrl', function($scope, routePick, $http, $q, stages, progress, session, $location){
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
      var completedDistance = 0;
      $scope.progressions = progressions;
      while (currentStage){
	if ($scope.progressions.hasOwnProperty(currentStage.id)
	    && hasProgressForStage){
	  completedDistance += $scope.progressions[currentStage.id].totalDistance;
	  if (!$scope.progressions[currentStage.id].completed){
	    $scope.distanceUntilNextGoal = currentStage.distance - $scope.progressions[currentStage.id].totalDistance;
	    hasProgressForStage = false;
	  }
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
  
  $scope.startRun = function(){
    session.startSession().then(
      function(){
	$location.path("/run/");
      },
      function(){
	console.log("failure");
      }
    );
  };
  
});
