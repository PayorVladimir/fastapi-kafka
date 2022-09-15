var map = new L.Map('map');
var linesLayer = new L.LayerGroup();
var ws = new WebSocket("ws://127.0.0.1:8002/consumer/stream");
var osmUrl = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    osm = new L.tileLayer(osmUrl, {maxZoom: 18});
var colors = ["#ff00ff", "#00fa40", "#f7ff00", "#e30012", "#bd93f9", "#ff5555", "#f1fa8c"];
map.setView([59.9311, 30.3609], 18).addLayer(osm);
lines = {};
map.on("zoomed", function (e) { linesLayer.clearLayers() });


ws.onmessage = function(event) {
    console.log(event.data)
    obj = JSON.parse(event.data)

    if(obj.type !== "message"){

          currentLocation= [obj.data.lat, obj.data.lon]
          if(! (obj.data.name in lines)) {
              lines[obj.data.name ] = {"location": []};

              lines[obj.data.name ]["config"] = {"color": colors[Math.floor(Math.random()*colors.length)]};
            }

      lines[obj.data.name ]["location"].push(currentLocation)

    if (!map.getBounds().contains(currentLocation)){
            map.setView(currentLocation)
    }

    line = L.polyline(lines[obj.data.name ]["location"], {"color": lines[obj.data.name]["config"]["color"]})
    linesLayer.addLayer(line)
    map.addLayer(linesLayer);
         }

};
