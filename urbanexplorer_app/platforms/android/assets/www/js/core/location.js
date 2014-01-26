'use strict';

UrbanExplorer.factory('geolocation', function ($rootScope, $q, $timeout) {
  var coordinates = [];
  
  var polling = false;
  var pollPositionTimeout = null;
  var watchPositionID = null;

  var getCurrentPosition = function () {
    var deferred = $q.defer();
    navigator.geolocation.getCurrentPosition(
      function (location) {
        $rootScope.$apply(function () {
	  console.log("LOCATION: Got.");
	  deferred.resolve(location);
        });
      }, function (error) {
        $rootScope.$apply(function () {
	  console.log("LOCATION: Error.");
          deferred.reject(error);
        });
      },
      {maximumAge: 0});
    return deferred.promise;
  }

  var pollPosition = function(){
    console.log("Poll called");
    if (!polling){
      polling = true;
      getCurrentPosition().then(
	function(coords){
	  if (polling){
	    coordinates.push([coords.coords.latitude, coords.coords.longitude]);
	    pollPosition();
	    // pollPositionTimeout = pollPosition();
	  }
	},
	function(error){
	  alert(error.code + " " + error.message);
	  console.log("retrying");
	  pollPositionTimeout = pollPosition();
	});
    }
  }

  function watchPosition(){
    if (polling){ return; }
    else {
      polling = true;
      watchPositionID = navigator.geolocation.watchPosition(
	function(location){
	  console.log("LOCATION WATCH: got coords.");
	  $rootScope.$apply(function(){
	    coordinates.push([location.coords.latitude, location.coords.longitude]);
	  });
	},
	function(error){
	  console.log("LOCATION WATCH: failed coords.");
	  alert(error.code + " " + error.message);
	},
	{
	  maximumAge: 0
	}
      );
    }
  }

  var cancelPolling = function(){
    polling = false;
    if (pollPositionTimeout){
      $timeout.cancel(pollPositionTimeout);
    }
    if (watchPositionID){
      navigator.geolocation.clearWatch(watchPositionID);
    }
  }

  var getCoordinatesList = function(){
    return coordinates;
  }

  return {
    getCurrentPosition: getCurrentPosition,
    pollPosition: pollPosition,
    getCoordinatesList: getCoordinatesList,
    watchPosition: watchPosition,
    cancelPolling: cancelPolling
  };
});
