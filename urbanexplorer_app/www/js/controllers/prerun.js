UrbanExplorer.controller('PrerunCtrl', function($scope, routePick, $http, $q, stages, progress, session, $location, routesCompleted, missions){
  "use strict";
  $scope.selected = routePick.get();
  
  $scope.stages = {};
  $scope.progressions = [];
  
  $scope.distanceRemain = 0;
  $scope.distanceUntilNextGoal = 0;

  $scope.starting = false;

  $scope.loading = true;

  var routeCompleted = routesCompleted.getRC($scope.selected.resource_uri);
  $scope.routeCompleted = routeCompleted;

  missions.getMissions().then(
    function(missions){
      angular.forEach(missions, function(mission){
	if (mission.resource_uri === $scope.selected.mission){
	  $scope.selected.mission = mission;
	  return;
	}
      });
    });

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
	  console.log(currentStage.resource_uri);
	  if ($scope.progressions.hasOwnProperty(currentStage.resource_uri)
	      && hasProgressForStage){
	    console.log("Has progress");
	    completedDistance += $scope.progressions[currentStage.resource_uri].totalDistance;
	    $scope.distanceUntilNextGoal -= $scope.progressions[currentStage.resource_uri].totalDistance;
	    $scope.distanceRemain += $scope.distanceUntilNextGoal;
	    if (!$scope.progressions[currentStage.resource_uri].completed){
	      hasProgressForStage = false;
	    }
	  }
	  else {
	    console.log("No progress");
	    hasProgressForStage = false;
	    $scope.distanceRemain += currentStage.distance;
	  }
	  console.log(currentStage.distance);
	  currentStage = $scope.stages[currentStage.nextStage]; 
	}
	$scope.loading = false;
      });    
  }

  $scope.startRun = function(){
    $scope.starting = true;
    session.startSession().then(
      function(){
	$location.path("/run/" + $scope.distanceUntilNextGoal +  "/");
      },
      function(failure){
	$scope.starting = false;
	console.log("failure");
	console.log(failure.data);
	alert("Please turn on your GPS and try again.");
      }
    );
  };

});
