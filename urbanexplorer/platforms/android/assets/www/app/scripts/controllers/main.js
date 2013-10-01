'use strict';

UrbanExplorer.factory('geolocation', function ($rootScope) {
  return {
    getCurrentPosition: function (onSuccess, onError, options) {
      navigator.geolocation.getCurrentPosition(
	function () {
          var that = this,
          args = arguments;
	  
          if (onSuccess) {
            $rootScope.$apply(function () {
              onSuccess.apply(that, args);
            });
          }
	}, function () {
          var that = this,
          args = arguments;
	  
          if (onError) {
            $rootScope.$apply(function () {
              onError.apply(that, args);
            });
          }
	},
	options);
    }
  };
});
UrbanExplorer.controller('MainCtrl', function($scope, geolocation) {
  $scope.awesomeThings = [
    'HTML5 Boilerplate',
    'AngularJS',
    'Testacular'
  ];

    geolocation.getCurrentPosition(function (position) {
      alert('Latitude: '              + position.coords.latitude          + '\n' +
            'Longitude: '             + position.coords.longitude         + '\n' +
            'Altitude: '              + position.coords.altitude          + '\n' +
            'Accuracy: '              + position.coords.accuracy          + '\n' +
            'Altitude Accuracy: '     + position.coords.altitudeAccuracy  + '\n' +
            'Heading: '               + position.coords.heading           + '\n' +
            'Speed: '                 + position.coords.speed             + '\n' +
            'Timestamp: '             + position.timestamp                + '\n');
    });

});
