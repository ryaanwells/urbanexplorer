UrbanExplorer.controller("RunCtrl", function($scope, geolocation){
  console.log("RUN");
  
  $scope.coords = null;

  geolocation.pollPosition();
  
  $scope.$watch(
    function(){
      return geolocation.getCoordinatesList();
    }, 
    function(newList, oldList){
      console.log(newList);
      $scope.coords = newList;
    },
    true
  );
});
