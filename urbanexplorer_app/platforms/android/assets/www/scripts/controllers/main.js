'use strict';

UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location, self) {
  console.log("Started MAIN");

  document.addEventListener('deviceready', function(){
    console.log("DEVICE READY");
  $scope.coords = [];

  //geolocation.pollPosition();

  $scope.self = "";

  self.getSelf().then(function(response){
    $scope.self = response;
  }, function(response){
    $scope.self = response;
  });

  $scope.swipeLeft = function(){
    $location.path("/targets/");
  }
  $scope.swipeRight = function(){
    $location.path("/achievements/");
  }
  /*
  $scope.$watch(
    function(){
      return geolocation.getCoordinatesList();
    }, 
    function(newList, oldList){
      console.log(newList);
      $scope.coords = newList;
    },
    true
  );
  */
  }, false);
});

UrbanExplorer.controller('TargetsCtrl' , function($scope, $location){
  $scope.swipeRight = function(){
    $location.path("/");
  }
});

UrbanExplorer.controller('AchievementsCtrl', function($scope, $location){
  $scope.swipeLeft = function(){
    $location.path("/");
  }
});
