'user strict';

UrbanExplorer.factory('self', function($q, $timeout, $http){

    console.log("HERE");
    
    var self = {};
    
    var getSelf = function(){
      var deferred = $q.defer();
      document.addEventListener('deviceready', function(){
	console.log(device.uuid);
	var getSelfURL = "http://ryaanwellsuni.pythonanywhere.com/getSelf/?deviceID=" + device.uuid;
	if (!self.hasOwnProperty("resource_uri")){
	  console.log("SELF: getting");
	  var config = {
	    method: "GET",
	    url: getSelfURL
	  }
	  $http(config).success(function(response){
	    console.log("SELF: succeeded");
	    self = response;
	    deferred.resolve(self);
	  }).error(function(response){
	    console.log("SELF: failed");
	    console.log(response);
	    deferred.reject(response);
	  });
	}
	else {
	  $timeout(function(){
	    deferred.resolve(self);
	  }, 0);
	}
      }, false);

      return deferred.promise;
    }
  
    return {
      getSelf: getSelf
    }

});

