UrbanExplorer.controller("PostRunCtrl", function($scope, session){
  console.log("Post run");
  $scope.session = session.getSession();
  console.log($scope.session.totalTime);
  $scope.session.seconds = Math.round($scope.session.totalTime / 1000.0) % 60;
  $scope.session.minutes = Math.round($scope.session.totalTime / (1000.0 * 60)) % 60;
  $scope.session.hours = Math.round($scope.session.totalTime / (1000.0 * 60 * 60));
  
  
});
