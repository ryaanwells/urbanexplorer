UrbanExplorer.controller("RunCtrl", function($scope, geolocation, session, $routeParams, $location, $timeout, routePick, routesCompleted, achievements){
  console.log("RUN");
  
  $scope.coords = [];
  
  var duration = 0;
  var now = 0;
  $scope.hours = 0; 
  $scope.minutes = 0;
  $scope.seconds = 0;

  $scope.distanceSoFar = 0;
  $scope.routeRemain = 0;
  
  $scope.nextAchievement = $routeParams.nextAchievement || 0;
  
  $scope.route = routePick.get();

  $scope.endConfirm = false;

  $scope.session = session.getSession();

  $scope.rc = routesCompleted.getRC($scope.route.resource_uri);

  $scope.percentRoute = 0;
  $scope.percentStage = 0;
  $scope.stageLength = 1;
  $scope.routeLength = 1;

  $scope.totalTime = 0;

  $scope.nextMedal = null;
  $scope.nextMedalTime = 0;

  var ach = {};
  achievements.get().then(function(achieve){
    angular.forEach(achieve[0], function(achievement){
      if (achievement.route == $scope.route.resource_uri){
	console.log(achievement.value);
	ach[achievement.value] = achievement;
      }
    });
    console.log(ach.G.metric);
  });
  

  geolocation.watchPosition(function(location){
    console.log(location.coords.latitude, location.coords.longitude, location.timestamp);
    // $scope.coords.push(location);
    session.updateSession(location)
      .then(function(data){
	$scope.coords.push(data);
	console.log(data.data.distance);
	console.log(data.data.distanceRemain);
	$scope.distanceSoFar = data.data.distance;
	$scope.routeRemain = data.data.routeDistanceRemain;
	$scope.nextAchievement = data.data.distanceRemain;

	$scope.distanceRemain = data.data.distanceRemain;
	$scope.stageLength = data.data.stageLength;
	$scope.routeDistanceRemain = data.data.routeDistanceRemain;
	$scope.routeLength = data.data.routeLength;
	$scope.percentRoute = Math.floor((($scope.routeLength - $scope.routeDistanceRemain) / $scope.routeLength) * 100);
	$scope.percentStage = Math.floor((($scope.stageLength - $scope.distanceRemain) / $scope.stageLength) * 100);
	
	$scope.totalTime = data.data.totalTime;

	angular.forEach(ach, function(achieve){
	  if (achieve.route == $scope.route.resource_uri){
	    if ($scope.totalTime < ach.G.metric){
	      console.log("GOLD");
	      $scope.nextMedal = ach.G;
	      $scope.nextMedalTime = ach.G.metric - $scope.totalTime;
	    }
	    else if ($scope.totalTime < ach.S.metric){
	      console.log("SILVER");
	      $scope.nextMedal = ach.S;
	      $scope.nextMedalTime = ach.S.metric - $scope.totalTime;
	    }
	    else if ($scope.totalTime < ach.B.metric){
	      console.log("BRONZE");
	      $scope.nextMedal = ach.B;
	      $scope.nextMedalTime = ach.B.metric - $scope.totalTime;
	    }
	    else {
	      $scope.nextMedal = null;
	      $scope.nextMedalTime = 0;
	    }
	  }
	});

	$scope.session = session.getSession();
      }, function(failure){
	console.log(failure);
      });
  });

  function startTimer(){
    now = new Date().getTime();
    setInterval(updateTime, 1000);
  }
  
  function updateTime(){
    var current = new Date().getTime();
    duration =  current - now;
    $scope.$apply(function(){
      $scope.seconds = parseInt(duration / 1000) % 60;
      if ($scope.seconds % 60 === 0){
	$scope.minutes++;
      }
      if ($scope.minutes + 1 % 61 === 0){
	$scope.minutes = 0;
	$scope.hours++;
      }
    });
  }

  startTimer();
  
  function end(){
    geolocation.cancelPolling();
    $location.path("/postRun/");
  }

  $scope.endSession = function(){
    if ($scope.endConfirm){
      end();
    }
    else {
      $scope.endConfirm = true;
    }
  };

});
