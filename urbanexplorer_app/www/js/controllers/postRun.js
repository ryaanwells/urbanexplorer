UrbanExplorer.controller("PostRunCtrl", function($scope, session){
  console.log("Post run");
  $scope.session = session.getSession();
});
