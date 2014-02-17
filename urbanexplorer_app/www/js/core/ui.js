UrbanExplorer.directive('maximise', function(){
  'use strict';
  return function($scope, $elem, $attrs){
    $elem.css('height', window.innerHeight - 76 + 'px');
    $elem.css('width',  window.innerWidth  + 'px');
  };
});


UrbanExplorer.directive('fill', function(){
  'use strict';
  return function($scope, $elem, $attrs){
    var pos = $elem[0].getBoundingClientRect();    
    $elem.css('height', window.innerHeight - pos.top + 'px');
    $elem.css('width', window.innerWidth + 'px');
    $elem.css('overflow-x', 'hidden');
    $elem.css('overflow-y', 'scroll');
  };
});
