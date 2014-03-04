UrbanExplorer.factory('self', function($q, $timeout, $http){
  'use strict';
  var self = {};
  
  var getSelf = function(clean){
    var deferred = $q.defer();

    console.log(device.uuid);
    
    var getSelfURL = "http://ryaanwellsuni.pythonanywhere.com/getSelf/?deviceID=" + device.uuid;

    if (!self.hasOwnProperty("resource_uri") || clean){
      console.log("SELF: getting");
      var config = {
	method: "GET",
	url: getSelfURL
      }
      $http(config).success(function(response){
	console.log("SELF: succeeded");
	self = response;
	var seconds = Math.floor(self.totalTime / 1000) % 60;
	var minutes = Math.floor(self.totalTime / (1000 * 60)) % 60;
	var hours = Math.floor(self.totalTime / (1000 * 60 * 60));
	self.time = {
	  seconds: seconds,
	  minutes: minutes,
	  hours: hours
	};
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
    
    return deferred.promise;
  }
  
  return {
    getSelf: getSelf
  }

});

