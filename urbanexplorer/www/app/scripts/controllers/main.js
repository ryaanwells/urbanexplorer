'use strict';

UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location) {
  /*
  geolocation.getCurrentPosition().then(function (position) {
    console.log(position);
    alert('Latitude: '              + position.coords.latitude          + '\n' +
          'Longitude: '             + position.coords.longitude         + '\n' +
          'Altitude: '              + position.coords.altitude          + '\n' +
          'Accuracy: '              + position.coords.accuracy          + '\n' +
          'Altitude Accuracy: '     + position.coords.altitudeAccuracy  + '\n' +
          'Heading: '               + position.coords.heading           + '\n' +
          'Speed: '                 + position.coords.speed             + '\n' +
          'Timestamp: '             + position.timestamp                + '\n');
  }, function(error){
    console.log(error.code);
    console.log(error.message);
  });
  */
  
  $scope.swipeLeft = function(){
    $location.path("/targets/");
  }
  $scope.swipeRight = function(){
    $location.path("/achievements/");
  }
  $scope.coords = function(){
    return geolocation.getCoordinatesList();
  }
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
