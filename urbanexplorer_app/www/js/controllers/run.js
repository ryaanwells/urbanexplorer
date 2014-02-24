UrbanExplorer.controller("RunCtrl", function($scope, geolocation, session, $routeParams, $location, $timeout){
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
  
  $scope.endConfirm = true;
  $timeout(function(){
    $scope.endConfirm = false;
  }, 20);

  $scope.session = session.getSession();

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
