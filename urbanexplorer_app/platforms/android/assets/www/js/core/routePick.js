UrbanExplorer.factory("routePick", function(){
  "use strict";
  
  var selectedRoute = {};
  
  function set(route){
    selectedRoute = route;
  }
  
  function get(){
    return selectedRoute;
  }
  
  return {
    set: set,
    get: get
  };
  
});
