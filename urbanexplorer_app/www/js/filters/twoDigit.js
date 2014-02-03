UrbanExplorer.filter("twoDigit", function(){
  "use strict";
  return function(input){
    if (angular.isString(input)){
      input = parseInt(input);
    }
    return input > 9 ? '' + input : '0' + input;
  }
});
