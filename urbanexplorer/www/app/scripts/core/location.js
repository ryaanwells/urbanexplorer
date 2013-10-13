'use strict';

UrbanExplorer.factory('geolocation', function ($rootScope, $q, $timeout) {
  var coordinates = [];
  
  var getCurrentPosition = function () {
    var deferred = $q.defer();
    navigator.geolocation.getCurrentPosition(
      function (location) {
        $rootScope.$apply(function () {
	  deferred.resolve(location);
        });
      }, function (error) {
        $rootScope.$apply(function () {
          deferred.reject(location);
        });
      },
      {enableHighAccuracy : true});
    return deferred.promise;
  }
  
  var pollPosition = function(){
    getCurrentPosition().then(
      function(coords){
	coordinates.push([coords.coords.latitude, coords.coords.longitude]);
	$timeout(pollPosition, 1000);
      },
      function(error){
	alert(error);
      });
  }

  var getCoordinatesList = function(){
    return coordinates;
  }

  return {
    pollPosition: pollPosition,
    getCoordinatesList: getCoordinatesList
  };
});
