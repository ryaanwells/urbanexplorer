UrbanExplorer.factory("session", function($q, $http, geolocation, routePick){
  "use strict";
  
  var session = null;

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

    if (!angular.isObject(session)){
      deferred.reject({
	reason: "No active session"
      });
    }
    
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
    
    $http(config).then(
      function(success){
	deferred.resolve(success);
	session = success.data;
      },
      function(failure){
	console.log(failure);
      });
    return deferred.promise;
    
  };

  function getSession(){
    return session;
  }

  function finalize(){
    var deferred = $q.defer();
    geolocation.getCurrentPosition().then(function(location){
      var config = {
	url: "http://ryaanwellsuni.pythonanywhere.com/updateSession/",
	method: "PATCH",
	data: {
	  sessionID: session.id,
	  lon: location.coords.longitude,
	  lat: location.coords.latitude,
	  timestamp: new Date(location.timestamp).getTime()
	}
      };
      $http(config).then(
	function(success){
	  deferred.resolve(success);
	  session = success.data;
	},
	function(failure){
	  console.log(failure);
	});
    }, function(failure){
      deferred.reject(failure);
    });
    return deferred.promise;
  }
  
  function endSession(){
    session = null;
  }
  
  return {
    startSession: startSession,
    updateSession: updateSession,
    getSession: getSession,
    finalize: finalize,
    endSession: endSession
  }
  
});
