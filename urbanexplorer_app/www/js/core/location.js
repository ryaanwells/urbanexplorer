UrbanExplorer.factory('geolocation', function ($rootScope, $q, $timeout) {
  'use strict';
  var coordinates = [];
  
  var polling = false;
  var pollPositionTimeout = null;
  var watchPositionID = null;

  var options = {
    maximumAge: 0,
    enableHighAccuracy: true
  };

  var getCurrentPosition = function(){
    var deferred = $q.defer();
    navigator.geolocation.getCurrentPosition(
      function (location) {
        $timeout(function(){
	  console.log("LOCATION: Got.");
	  deferred.resolve(location);
        });
      }, function (error) {
        $timeout(function(){
	  console.log("LOCATION: Error.");
          deferred.reject(error);
        });
      },
      options
    );
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
	}
      );
    }
  }

  function watchPosition(callback){
    if (polling){ return; }
    else {
      polling = true;
      watchPositionID = navigator.geolocation.watchPosition(
	function(location){
	  console.log("LOCATION WATCH: got coords.");
	  $timeout(function(){
	    coordinates.push([location.coords.latitude, location.coords.longitude]);
	    callback(location);
	  });
	},
	function(error){
	  console.log("LOCATION WATCH: failed coords.");
	  alert(error.code + " " + error.message);
	},
	options
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
