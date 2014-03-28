var UrbanExplorer = angular.module('UrbanExplorer', ['ngRoute','ngTouch'])
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
      .when('/run/:nextAchievement/', {
	templateUrl: 'html/run.html',
	controller: 'RunCtrl'
      })
      .when('/postRun/', {
	templateUrl: 'html/postRun.html',
	controller: 'PostRunCtrl',
      })
      .when('/help/', {
	templateUrl: 'html/help.html'
      })
      .otherwise({
        redirectTo: '/'
      });
  }])
  .run(['$rootScope', '$location', 'routePick', 'session', 'self', function($rootScope, $location, routePick, session, self){
    'use strict';
    $rootScope.$on("$locationChangeStart", function(event, next, current){
      if (next.indexOf("/run/") >= 0 &&
	  current.indexOf("/prerun/") < 0){
	if (routePick.get().hasOwnProperty("resource_uri")){
	  $location.path("/prerun/");
	}
	else {
	  $location.path("/targets/");
	}
      }
      else if (current.indexOf("/postRun/") >=0 &&
	       next.indexOf("/postRun/") < 0){
	console.log("Leaving postRun");
	session.endSession();
	self.getSelf(true);
      }
    });
  }]);
