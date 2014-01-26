var UrbanExplorer = angular.module('UrbanExplorer', ['ngRoute','ngTouch', 'ui.bootstrap'])
  .config(['$routeProvider', function($routeProvider) {
    'use strict';
    $routeProvider
      .when('/', {
        templateUrl: 'html/main.html',
        controller: 'MainCtrl'
      })
      .when('/targets/', {
	templateUrl: 'html/targets.html',
	controller: 'TargetsCtrl'
      })
      .when('/achievements/', {
	templateUrl: 'html/achievements.html',
	controller: 'AchievementsCtrl'
      })
      .when('/prerun/', {
	templateUrl: 'html/prerun.html',
	controller: 'PrerunCtrl'
      })
      .when('/run/', {
	templateUrl: 'html/run.html',
	controller: 'RunCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);