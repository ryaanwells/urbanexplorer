UrbanExplorer.controller("navbar", function($scope, $location){
  
  $scope.isActive = function(partial){
    if (partial === '/'){
      return ($location.path() === partial);
    }
    return ($location.path().indexOf(partial) >= 0);
  };

});
