UrbanExplorer.controller("RunCtrl", function($scope, geolocation, session){
  console.log("RUN");
  
  $scope.coords = [];
  
  var duration = 0;
  var now = 0;
  $scope.hours = 0; 
  $scope.minutes = 0;
  $scope.seconds = 0;
  
  geolocation.watchPosition(function(location){
    console.log(location.coords.latitude, location.coords.longitude, location.timestamp);
    $scope.coords.push(location);
    session.updateSession(location);
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
      if ($scope.minutes % 60 === 0){
	$scope.hours++;
      }
    });
  }

  startTimer();
  
  // $scope.$watch(
  //   function(){
  //     return geolocation.getCoordinatesList();
  //   }, 
  //   function(newList, oldList){
  //     console.log(newList);
  //     $scope.coords = newList;
  //   },
  //   true
  // );
});
