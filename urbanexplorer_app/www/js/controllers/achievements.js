UrbanExplorer.controller('AchievementsCtrl', function($scope, $location, achievements){
  "use strict";
  
  $scope.achievements = [];
  
  achievements.get().then(
    function(all){
      $scope.achievements = all[0];
      angular.forEach(all[1], function(userAch){
	angular.forEach(all[0], function(ach){
	  if (userAch.achievementID == ach.resource_uri){
	    ach.complete = true;
	    ach.date = userAch.completionDate;
	    return;
	  }
	  ach.complete = false;
	});
      });
    });
});
