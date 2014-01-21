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
      .when('/prerun/', {
	templateUrl: 'views/prerun.html',
	controller: 'PrerunCtrl'
      })
      .when('/run/', {
	templateUrl: 'views/run.html',
	controller: 'RunCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);
