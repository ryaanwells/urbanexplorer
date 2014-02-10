UrbanExplorer.controller('AchievementsCtrl', function($scope, $location, achievements){
  "use strict";
  $scope.swipeLeft = function(){
    $location.path("/");
  };

  $scope.all = [];

  achievements.get().then(
    function(all){
      $scope.all = all;
    });

});
