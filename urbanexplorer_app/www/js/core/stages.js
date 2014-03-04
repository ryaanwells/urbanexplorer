UrbanExplorer.factory('stages', function($q, $http, $timeout){
  'use strict';

  var stages = {};

  function getStages(resources){
    var deferred = $q.defer();
    var waiting = [];
    var found = {};
    var temp = "";
    var i;
    
    for (i = 0; i < resources.length; i++){
      if (stages.hasOwnProperty(resources[i])){
	found[resources[i]] = stages[resources[i]];
      }
      else {
	waiting.push(resources[i]);
      }
    }
    
    if (waiting.length > 0){
      var query = "";
      for (i = 0; i < waiting.length; i++){
	temp = waiting[i].substr(0, waiting[i].lastIndexOf('/'));
	query += temp.substr(temp.lastIndexOf('/') + 1);
	if (i + 1 < waiting.length){
	  query += ";";
	}
      }
      var config = {
	method: "GET",
	url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/stage/set/" + query + "/"
      }
      console.log(config.url);
      $http(config).success(function(result){
	console.log("Objects Returned: " + result.objects.length);
	for (i = 0; i < result.objects.length; i++){
	  console.log(result.objects[i].resource_uri);
	  stages[result.objects[i].resource_uri] = result.objects[i];
	   found[result.objects[i].resource_uri] = result.objects[i];
	}
	deferred.resolve(found);
      }).error(function(result){
	console.log("STAGES: failure");
	deferred.reject({});
      });
    }
    else {
      $timeout(function(){
	deferred.resolve(found);
      }, 0);
    }
    return deferred.promise;
  }

  function getAll(){
    var deferred = $q.defer();
    var config = {
      url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/stage/?limit=0",
      method: "GET"
    };
    $http(config).success(function(result){
      stages = result.objects;
      deferred.resolve(stages);
    }).error(function(result){
      console.log("STAGES: failure all");
      deferred.reject({});
    });
    return deferred.promise;
  }
  
  return {
    getStages: getStages,
    getAll: getAll
  };

});
