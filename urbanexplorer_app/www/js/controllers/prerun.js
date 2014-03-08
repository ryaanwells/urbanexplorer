UrbanExplorer.controller('PrerunCtrl', function($scope, routePick, $http, $q, stages, progress, session, $location, routesCompleted, missions, achievements){
  "use strict";
  $scope.selected = routePick.get();
  
  $scope.stages = {};
  $scope.progressions = [];
  
  $scope.distanceRemain = 0;
  $scope.distanceUntilNextGoal = 0;
  $scope.distanceOnStage = 0;


  $scope.timeSoFar = 0;

  $scope.starting = false;

  $scope.loading = true;

  $scope.percentRoute = 0;
  $scope.percentStage = 0;

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

  $scope.back = function(){
    $location.path("/targets/");
  };

  $scope.times = {
    gold: 0,
    silver: 0,
    bronze: 0
  }

  $scope.done = {
    gold: false,
    silver: false,
    bronze: false
  }

  achievements.get().then(function(achievements){
    angular.forEach(achievements[0], function(ach){
      if (ach.route == $scope.selected.resource_uri){
	if (ach.value === "B"){
	  $scope.times.bronze = ach.metric;
	  $scope.done.bronze = ach.completed;
	}
	else if (ach.value === "S"){
	  $scope.times.silver = ach.metric;
	  $scope.done.silver = ach.completed;
	}
	else if (ach.value === "G"){
	  $scope.times.gold = ach.metric;
	  $scope.done.gold = ach.completed;
	}
      }
    });
  });
  
  if (routeCompleted){
    $scope.distanceUntilNextGoal = routeCompleted.currentJourney.progress.stageID.distance - routeCompleted.currentJourney.progress.totalDistance;
    $scope.distanceOnStage = routeCompleted.currentJourney.progress.stageID.distance;
    var accDistance = 0;
    var accTime = 0;
    angular.forEach(routeCompleted.currentJourney.allProgress, function(progress){
      accDistance += progress.totalDistance;
      accTime += progress.totalTime;
    });
    $scope.timeSoFar = accTime;
    $scope.distanceRemain = $scope.selected.length - accDistance;

    $scope.percentRoute = Math.floor((accDistance / $scope.selected.length) * 100);
    $scope.percentStage = Math.floor((routeCompleted.currentJourney.progress.totalDistance / 
				      routeCompleted.currentJourney.progress.stageID.distance) * 100);
    console.log("completed");
    $scope.loading = false;
  }
  else {
    angular.forEach($scope.selected.stages, function(stage){
      if (stage.resource_uri == $scope.selected.startStage){
	$scope.distanceUntilNextGoal = stage.distance;
	$scope.distanceOnStage = stage.distance;
      }
      $scope.distanceRemain += stage.distance;
    });
    $scope.timeSoFar = 0;
    $scope.percentRoute = 0;
    $scope.percentStage = 0;
    $scope.loading = false;
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
