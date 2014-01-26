UrbanExplorer.factory('routes', function($q, $http, $timeout){
  'use strict';
  
  var routes = [];

  var routesByMission = {};

  function getRoutes(){
    var deferred = $q.defer();

    if (routes.length === 0){
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
      }).error(function(response){
	console.log("ROUTES: failure");
	console.log(response);
	deferred.resolve([]);
      });
    }
    else {
      $timeout(function(){
	deferred.resolve(routes);
      }, 0);
    }
    return deferred.promise;
  };

  function getRoutesForMission(mission){
    for (var key in routesByMission){
      console.log(key);
    }
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
