UrbanExplorer.factory('routes', function($q, $http, $timeout){
  'use strict';
  
  var routes = [];

  var routesByMission = {};
  
  var getting = false;
  var pendingRequests = [];

  function getRoutes(){
    var deferred = $q.defer();

    if (getting){
      pendingRequests.push(deferred);
      return deferred.promise;
    }
    else if (routes.length > 0){
      deferred.resolve(routes);
    }
    else{
      getting = true;
      var config = {
	method: "GET",
	url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/route/?limit=0"
      }
      $http(config).success(function(response){
	console.log("ROUTES: success");
	routes = response.objects;
	for (var i = 0; i< routes.length; i++){
	  if (routesByMission.hasOwnProperty(routes[i].mission)){
	    routesByMission[routes[i].mission].push(routes[i]);
	  }
	  else {
	    routesByMission[routes[i].mission] = [routes[i]];
	  }
	}
	deferred.resolve(routes);
	getting = false;
      }).error(function(response){
	console.log("ROUTES: failure");
	console.log(response);
	deferred.resolve([]);
	getting = false;
      });
    }

    return deferred.promise;
  };

  function getRoutesForMission(mission){
    if (routesByMission.hasOwnProperty(mission)){
      return routesByMission[mission];
    }
    else {
      return [];
    }
  }

  return {
    getRoutes: getRoutes,
    getRoutesForMission: getRoutesForMission
  }
  
});
