UrbanExplorer.controller("PostRunCtrl", function($scope, session){
  console.log("Post run");
  $scope.session = session.getSession();
  // console.log($scope.session.totalTime);
  $scope.session.seconds = Math.floor($scope.session.totalTime / 1000.0) % 60;
  $scope.session.minutes = Math.floor($scope.session.totalTime / (1000.0 * 60)) % 60;
  $scope.session.hours = Math.floor($scope.session.totalTime / (1000.0 * 60 * 60));
  
  
});
