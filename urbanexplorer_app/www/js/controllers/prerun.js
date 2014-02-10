UrbanExplorer.controller('PrerunCtrl', function($scope, routePick, $http, $q, stages, progress, session, $location, routesCompleted){
  "use strict";
  $scope.selected = routePick.get();
  
  $scope.stages = {};
  $scope.progressions = [];
  
  $scope.distanceRemain = 0;
  $scope.distanceUntilNextGoal = 0;

  $scope.starting = false;

  var routeCompleted = routesCompleted.getRC($scope.selected.resource_uri);
  $scope.routeCompleted = routeCompleted;

  if (routeCompleted && routeCompleted.completed){
    console.log("completed");
  }
  else {
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
	  if (hasProgressForStage){
	    $scope.distanceUntilNextGoal = currentStage.distance;
	  }
	  if ($scope.progressions.hasOwnProperty(currentStage.id)
	      && hasProgressForStage){
	    completedDistance += $scope.progressions[currentStage.id].totalDistance;
	    $scope.distanceUntilNextGoal -= $scope.progressions[currentStage.id].totalDistance;
	    $scope.distanceRemain += $scope.distanceUntilNextGoal;
	    if (!$scope.progressions[currentStage.id].completed){
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
      });    
  }

  $scope.startRun = function(){
    $scope.starting = true;
    session.startSession().then(
      function(){
	$location.path("/run/" + $scope.distanceUntilNextGoal +  "/");
      },
      function(failure){
	console.log("failure");
	console.log(failure.data);
      }
    );
  };

});
