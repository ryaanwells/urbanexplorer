UrbanExplorer.factory("achievements", function($q, $http, self){
  var allAchievements = [];
  var userAchievements = [];

  var getting = false;
  var pendingRequests = [];

  function getAchievements(){
    var deferred = $q.defer();
  };

  function get(){
    var deferred = $q.defer();
    if (allAchievements.length > 0){
      deferred.resolve([allAchievements, userAchievements]);
    }
    var config = {
      url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/achievement/?limit=0",
      method: "GET"
    };
    var user_achievements = {
      url: "http://ryaanwellsuni.pythonanywhere.com/api/v1/userAchievement/?limit=0",
      method: "GET"
    };
    self.getSelf()
      .then(
	function(s){
	  user_achievements.url += "&userID=" + s.deviceID;
	  return $q.all([$http(config), $http(user_achievements)])
	})
      .then(
	function(done){
	  allAchievements = done[0].data.objects;
	  userAchievements = done[1].data.objects;
	  deferred.resolve([allAchievements, userAchievements]);
	});
    return deferred.promise;
  }

  return {
    get: get
  }
});
