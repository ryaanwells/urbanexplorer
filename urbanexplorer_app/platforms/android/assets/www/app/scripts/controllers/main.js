'use strict';

UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location) {

  $scope.coords = [];

  geolocation.pollPosition();
  $scope.swipeLeft = function(){
    $location.path("/targets/");
  }
  $scope.swipeRight = function(){
    $location.path("/achievements/");
  }
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
