UrbanExplorer.factory("session", function($q, $http, $location, routePick){
  "use strict";
  
  var session = null;

  function startSession(){
    var config;
    var deferred = $q.defer();
    if (session === null){
      config = {
	url: "http://ryaanwellsuni.pythonanywhere.com/startSession/",
	method: "POST",
	data: {
	  routeID: routePick.get().id,
	  deviceID: device.uuid
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
	  console.log(failure.data);
	});
    }
    else {
      deferred.resolve();
    }
    return deferred.promise;
  };
  
  return {
    startSession: startSession
  }

});
