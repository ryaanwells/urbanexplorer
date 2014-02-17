UrbanExplorer.directive("achievementView", function(){
  "use strict";
  return {
    templateUrl: "html/directives/achievementView.html",
    replace: true,
    restrict: 'E',
    scope: {
      ach: '='
    },
    link: function($scope, $elem, $attrs){
      $scope.open = false;

      $scope.toggle = function(){
	$scope.open = !$scope.open;
      }
    }
  };
});
