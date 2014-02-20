UrbanExplorer.factory('progress', function($q, $http, $timeout, self){
  "use strict";
  
  var progressions = {};

  function getProgressions(stages, update){
    var deferred = $q.defer();
    var waiting = [];
    var found = {};
    var i;
    var query;
    var config;
    if (update){ // Update all, ignore "cache"
      waiting = stages;
    }
    else {
      for (i in stages){
	if (stages.hasOwnProperty(i) && stages[i] &&
	    progressions.hasOwnProperty(stages[i].resource_uri)){
	  console.log("FOUND");
	  found[stages[i].resource_uri] = progressions[stages[i].resource_uri];
	}
	else {
	  waiting.push(stages[i].id);
	}
      }
    }

    if (waiting.length > 0){
      query = "";
      for (i = 0; i < waiting.length; i++){
	query += "stageID__in=" + waiting[i];
	if (i + 1 < waiting.length){
	  query += "&";
	}
      }
      config = {
	method: "GET",

	url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/progress/?" + query
      };
      self.getSelf()
	.then(function(s){
	  config.url += "&userID=" + s.deviceID;
	  $http(config).success(function(result){
	    for (i = 0; i < result.objects.length; i++){
	      progressions[result.objects[i].stageID] = result.objects[i];
	      found[result.objects[i].stageID] = result.objects[i];
	    }
	    deferred.resolve(found);
	  }).error(function(result){
	    console.log("PROGRESS: failure");
	    console.log(result);
	    deferred.reject("fail");
	  });
	});
    }
    
    else {
      $timeout(function(){
	deferred.resolve(found);
      }, 0);
    }
    
    return deferred.promise;
  }

  return {
    getProgressions: getProgressions
  };
  
});
