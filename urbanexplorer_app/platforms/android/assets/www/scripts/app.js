var UrbanExplorer = angular.module('UrbanExplorer', ['ngRoute','ngTouch', 'ui.bootstrap'])
  .config(['$routeProvider', function($routeProvider) {
    'use strict';
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/targets/', {
	templateUrl: 'views/targets.html',
	controller: 'TargetsCtrl'
      })
      .when('/achievements/', {
	templateUrl: 'views/achievements.html',
	controller: 'AchievementsCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);
