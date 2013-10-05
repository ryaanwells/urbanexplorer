'use strict';

var UrbanExplorer = angular.module('UrbanExplorer', ['ngRoute','ngTouch', 'ui.bootstrap'])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/other/', {
	templateUrl: 'views/other.html',
	controller: 'OtherCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);
