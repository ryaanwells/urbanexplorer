UrbanExplorer.filter("time", function(){
  "use strict";
  return function(input){
    var seconds, minutes, hours;
    if (angular.isString(input)){
      input = parseFloat(input);
    }
    seconds = Math.floor(input / 1000) % 60;
    minutes = Math.floor(input / (1000 * 60)) % 60;
    hours = Math.floor(input / (1000 * 60 * 60));

    seconds = seconds < 10 ? '0' + seconds : seconds; 
    minutes = minutes < 10 ? '0' + minutes : minutes;
    hours = hours < 10 ? '0' + hours : hours;
    return hours + ":" + minutes + ":" + seconds
  }
});
