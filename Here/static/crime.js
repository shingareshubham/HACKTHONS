
// Initialize the platform object:
var platform = new H.service.Platform({
    'apikey': 'euCjRuuBXFTB_CmP1JI3XdIyw8lORU-RfYE9PfIMi2g'
});

// Obtain the default map types from the platform object
var maptypes = platform.createDefaultLayers();


console.log('insight')
// Instantiate (and display) a map object:
var map = new H.Map(
    document.getElementById('mapContainer'),
    maptypes.vector.normal.map,
    {
        zoom: 12,
        center: { lat: 19.0621, lng: 72.8834 }
    });

// add a resize listener to make sure that the map occupies the whole container
window.addEventListener('resize', () => map.getViewPort().resize());
console.log('insight')
//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));


var icon_dollar = new H.map.Icon("/images/dollar.png");
var icon_robber = new H.map.Icon("/images/robber-car.png");
var icon_domestic = new H.map.Icon("/images/hand-print.png");
var icon_criminal = new H.map.Icon("/images/violent-criminal.png");

//var marker_dollar = "";
for (var i = 0; i < locations.length; i++) {
    //console.log(locations[i][0]);
    if (locations[i][0] == 'thief') {
        var marker_dollar = new H.map.Marker({ lat: locations[i][1], lng: locations[i][2] }, { icon: icon_dollar });
        console.log('inside loop', locations[i][0], 'lat:', locations[i][1], 'long:', locations[i][2]);
        map.addObject(marker_dollar);
    }
    else if (locations[i][0] == 'robber') {
        var marker_robber = new H.map.Marker({ lat: locations[i][1], lng: locations[i][2] }, { icon: icon_robber });
        map.addObject(marker_robber);
    }
    else if (locations[i][0] == 'rape') {
        var marker_domestic = new H.map.Marker({ lat: locations[i][1], lng: locations[i][2] }, { icon: icon_domestic });
        map.addObject(marker_domestic);
    }
    else if (locations[i][0] == 'violent_crime') {
        var marker_criminal = new H.map.Marker({ lat: locations[i][1], lng: locations[i][2] }, { icon: icon_criminal });
        map.addObject(marker_criminal);
    }

}