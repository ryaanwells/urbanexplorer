UrbanExplorer.factory('routesCompleted', function($q, $http, $timeout, self){
  'use strict';
  
  var routesCompleted = {};

  var getting = false;
  var pendingRequests = [];

  function getCompleted(){
    var deferred = $q.defer();

    if (getting){
      pendingRequests.push(deferred);
      return deferred.promise;
    }
    else {
      getting = true;
      var config = {
	method: "GET",
	url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/routesCompleted/?limit=0"
      }
      self.getSelf()
	.then(function(self){
	  config.url += "&userID=" + self.deviceID
	  return $http(config);
	})
	.then(function(success){
	  var rc = success.data.objects;
	  for (var i = 0; i < rc.length; i++){
	    routesCompleted[rc[i].routeID] = rc[i];
	  }
	  deferred.resolve(routesCompleted);
	  getting = false;
	  for (var i = 0; i < pendingRequests.length; i++){
	    pendingRequests[i].resolve(routesCompleted);
	  }
	  console.log("done");
	});
    }
    return deferred.promise;
  }

  function getRC(route_uri){
    return routesCompleted[route_uri];
  }
  
  return {
    getCompleted: getCompleted,
    getRC: getRC
  }

});
