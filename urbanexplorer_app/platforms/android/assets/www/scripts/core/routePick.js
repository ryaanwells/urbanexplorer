UrbanExplorer.factory("routePick", function(){
  "use strict";
  
  var selectedRoute = {};
  
  function set(route){
    selectedRoute = route;
  }
  
  function get(){
    return selectedRoute;
  }
  
  function register(fn){
    callbacks.push(fn);
  }
  
  return {
    set: set,
    get: get
  };
  
});
