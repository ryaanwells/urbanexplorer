UrbanExplorer.factory("session", function($q, $http, geolocation, routePick){
  "use strict";
  
  var session = null;
  var sendingUpdate = false;
  var pending = [];

  function startSession(){
    var config;
    var deferred = $q.defer();
    if (session === null){
      geolocation.getCurrentPosition().then(
	function(success){
          config = {
	    url: "http://ryaanwellsuni.pythonanywhere.com/startSession/",
	    method: "POST",
	    data: {
	      routeID: routePick.get().id,
	      deviceID: device.uuid,
	      lat: success.coords.latitude,
	      lon: success.coords.longitude,
	      timestamp: new Date(success.timestamp).getTime()
	    }
	  };
	  console.log(routePick.get().id);
	  console.log(device.uuid);
	  $http(config).then(
	    function(success){
	      session = success.data;
	      console.log("SESSION: created successfully");
	      deferred.resolve();
	    },
	    function(failure){
	      deferred.reject(failure);
	    });
	},
	function(failure){
	  console.log(failure);
	  deferred.reject(failure);
	});
    }
    else {
      deferred.resolve();
    }
    return deferred.promise;
  };
  
  function updateSession(location){
    var config;
    var deferred = $q.defer();
    
    config = {
      url: "http://ryaanwellsuni.pythonanywhere.com/updateSession/",
      method: "PATCH",
      data: {
	sessionID: session.id,
	lon: location.coords.longitude,
	lat: location.coords.latitude,
	timestamp: new Date(location.timestamp).getTime()
      }
    }
    console.log(config.data.sessionID);
    console.log(config.data.lon);
    console.log(config.data.lat);
    console.log(config.data.timestamp);
    $http(config).then(
      function(success){
	deferred.resolve();
      },
      function(failure){
	console.log(failure);
      });
    return deferred.promise;
    
  };
  
  return {
    startSession: startSession,
    updateSession: updateSession
  }
  
});
