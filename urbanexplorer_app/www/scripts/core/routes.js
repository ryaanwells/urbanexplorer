'use strict';

UrbanExplorer.factory('routes', function($q, $http, $timeout){
  
  var routes = [];

  var getRoutes = function(){
    var deferred = $q.defer();

    if (routes.length === 0){
      var config = {
	method: "GET",
	url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/stage/?limit=0"
      }
      $http(config).success(function(response){
	console.log("ROUTES: success");
	routes = response.objects;
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

  return {
    getRoutes: getRoutes
  }
  
});
