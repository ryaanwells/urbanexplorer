UrbanExplorer.controller("PrerunCtrl", function($scope, routePick, $http, $q, stages){
  $scope.selected = routePick.get();
  
  $scope.stages = $scope.selected.stages;

  stages.getStages($scope.selected.stages).then(function(result){
    $scope.stages = result;
  });
});
