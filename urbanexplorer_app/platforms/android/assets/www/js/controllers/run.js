UrbanExplorer.controller("RunCtrl", function($scope, geolocation, session){
  console.log("RUN");
  
  $scope.coords = [];

  geolocation.watchPosition(function(location){
    console.log(location.coords.latitude, location.coords.longitude, location.timestamp);
    $scope.coords.push(location);
    session.updateSession(location);
  });
  
  // $scope.$watch(
  //   function(){
  //     return geolocation.getCoordinatesList();
  //   }, 
  //   function(newList, oldList){
  //     console.log(newList);
  //     $scope.coords = newList;
  //   },
  //   true
  // );
});
