'use strict';

UrbanExplorer.factory('geolocation', function ($rootScope, $q, $timeout) {
  var coordinates = [];
  
  var polling = false;
  var pollPositionTimeout = null;

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
    if (!polling){
      polling = true;
      getCurrentPosition().then(
	function(coords){
	  if (polling){
	    coordinates.push([coords.coords.latitude, coords.coords.longitude]);
	    pollPositionTimeout = $timeout(pollPosition, 10000);
	  }
	},
	function(error){
	  alert(error);
	});
    }
  }

  var cancelPolling = function(){
    polling = false;
    $timeout.cancel(pollPositionTimeout);
  }

  var getCoordinatesList = function(){
    return coordinates;
  }

  return {
    pollPosition: pollPosition,
    getCoordinatesList: getCoordinatesList,
    cancelPolling: cancelPolling
  };
});
