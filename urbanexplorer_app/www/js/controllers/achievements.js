UrbanExplorer.controller('AchievementsCtrl', function($scope, $location, achievements, progress, stages, routes, missions){
  "use strict";
  
  $scope.achievements = [];

  $scope.ach = {};

  $scope.missions = [];

  missions.getMissions().then(function(missions){
    $scope.missions = missions;
  });

  // $scope.prog = {};
  // stages.getAll().then(function(stages){
  //   progress.getAll().then(function(progressions){
  //     $scope.prog = progressions;
  //     angular.forEach($scope.prog, function(progress){
  // 	if (progress.completed || !$scope.ach.hasOwnProperty(progress.stageID.resource_uri)){
  // 	  $scope.ach[progress.stageID.resource_uri] = progress;
  // 	}
  //     });
  //   });
  // });
  
  // achievements.get().then(
  //   function(all){
  //     $scope.achievements = all[0];
  //     angular.forEach(all[1], function(userAch){
  // 	angular.forEach(all[0], function(ach){
  // 	  if (userAch.achievementID == ach.resource_uri){
  // 	    ach.complete = true;
  // 	    ach.date = userAch.completionDate;
  // 	    return;
  // 	  }
  // 	  ach.complete = false;
  // 	});
  //     });
  //   });
});
