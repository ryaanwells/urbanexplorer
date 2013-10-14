'use strict';

UrbanExplorer.factory('geolocation', function ($rootScope) {
  return {
    getCurrentPosition: function (onSuccess, onError, options) {
      navigator.geolocation.getCurrentPosition(
	function () {
          var that = this,
          args = arguments;
	  console.log("Success callback");
          if (onSuccess) {
	    console.log("success");
            $rootScope.$apply(function () {
              onSuccess.apply(that, args);
            });
          }
	}, function () {
          var that = this,
          args = arguments;
	  console.log("Failure callback");
          if (onError) {
	    console.log("fail");
            $rootScope.$apply(function () {
              onError.apply(that, args);
            });
          }
	},
	{enableHighAccuracy : true});
    }
  };
});
UrbanExplorer.controller('MainCtrl', function($scope, geolocation, $location) {
  $scope.awesomeThings = [
    'HTML5 Boilerplate',
    'AngularJS',
    'Testacular'
  ];
  console.log("here");
  geolocation.getCurrentPosition(function (position) {
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
  
  $scope.swipeLeft = function(){
    $location.path("/other/");
  }
});
 
UrbanExplorer.controller('OtherCtrl' , function($scope, $location){
  alert("HERE");
  $scope.swipeRight = function(){
    $location.path("/");
  }
});