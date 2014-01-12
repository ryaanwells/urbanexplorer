UrbanExplorer.controller('AchievementsCtrl', function($scope, $location){
  "use strict";
  $scope.swipeLeft = function(){
    $location.path("/");
  };

});
