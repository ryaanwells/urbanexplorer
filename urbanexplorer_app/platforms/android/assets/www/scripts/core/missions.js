UrbanExplorer.factory("missions", function($q, $http, $timeout){
  "use strict";
  var missions = [];

  function getMissions(){
    var deferred = $q.defer();
    if (missions.length == 0){
      var config = {};
      config.url = "http://ryaanwellsuni.pythonanywhere.com/api/v1/mission/?limit=0";
      config.method = "GET";
      $http(config).success(function(response){
	console.log("MISSIONS: success");
	missions = response.objects;
	deferred.resolve(missions);
      }).error(function(response){
	console.log("MISSIONS: failure");
	deferred.reject(response);
      });
    }
    else {
      $timeout(function(){
	deferred.resolve(missions);
      }, 0);
    }
    return deferred.promise
  }

  return {
    getMissions: getMissions
  }
  
});
