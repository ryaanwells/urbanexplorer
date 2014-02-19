UrbanExplorer.controller('TargetsCtrl' , function($scope, $location, routePick, missions){
  "use strict";
  $scope.swipeRight = function(){
    $location.path("/");
  }
  
  $scope.$watch(routePick.get, function(newRoute, oldRoute){
    console.log("TARGET: changed");
    console.log(newRoute.name);
    $scope.selected = newRoute;
  }, true);
  
  $scope.selected = routePick.get();
  
  $scope.missions = [];

  missions.getMissions().then(function(response){
    $scope.missions = response;
  }, function(response){
    $scope.missions = response;
  });

  $scope.start = function(){
    $location.path("/prerun/");
  };

});
