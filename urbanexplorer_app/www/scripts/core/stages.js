UrbanExplorer.factory('stages', function($q, $http, $timeout){
  'use strict';

  var stages = {};

  function getStages(resources){
    var deferred = $q.defer();
    var waiting = [];
    var found = [];
    var temp = "";
    var i;
    
    for (i = 0; i < resources.length; i++){
      if (!stages.hasOwnProperty(resources[i])){
	temp = resources[i].substr(0, resources[i].lastIndexOf('/'));
	waiting.push([temp.substr(temp.lastIndexOf('/') + 1), i]);
	found.push(null);
      }
      else {
	found.push(stages[resources[i]]);
      }
    }
    
    if (waiting.length > 0){
      var query = "";
      for (i = 0; i < waiting.length; i++){
	query += waiting[i][0];
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
	for (i = 0; i < result.objects.length; i++){
	  stages[result.objects[i].resource_uri] = result.objects[i];
	  found[waiting[i][1]] = result.objects[i];
	}
	deferred.resolve(found);
      }).error(function(result){
	console.log("STAGES: failure");
	deferred.reject("fail");
      });
    }
    else{
      $timeout(function(){
	deferred.resolve(found);
      }, 0);
    }
    return deferred.promise;
  }
  
  return {
    getStages: getStages
  };

});
