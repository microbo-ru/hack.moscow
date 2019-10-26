<template>
  <div class="here-map">
    <div ref="map" v-bind:style="{ width: width, height: height }"></div>
  </div>
</template>

<script>
function getCoordByName(name) {
  return fetch(
    `https://geocode-maps.yandex.ru/1.x/?apikey=2d121788-cbff-41a5-9cfb-62e349951e8b&format=json&geocode=${name}`
  ).then(response => {
    if (response.ok) {
      return response.json().then(json => {
        console.log(json);
        return json.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos
          .split(" ")
          .map(parseFloat);
      });
    }
  });
}

function addCircleMarker(name, map, behavior, H) {
  getCoordByName(name).then(function(res) {
    console.log(res);
    var circle = new H.map.Circle({ lat: res[1], lng: res[0] }, 8000);
    map.addObject(circle);
    addDraggableMarker(map, behavior, H, res[1], res[0]); //    menyaem mestami
  });
}
function addDraggableMarker(map, behavior, H, _lat, _lng) {
  var marker = new H.map.Marker(
    { lat: _lat, lng: _lng },
    {
      // mark the object as volatile for the smooth dragging
      volatility: true
    }
  );
  // Ensure that the marker can receive drag events
  marker.draggable = true;
  map.addObject(marker);

  // disable the default draggability of the underlying map
  // and calculate the offset between mouse and target's position
  // when starting to drag a marker object:
  map.addEventListener(
    "dragstart",
    function(ev) {
      var target = ev.target,
        pointer = ev.currentPointer;
      if (target instanceof H.map.Marker) {
        var targetPosition = map.geoToScreen(target.getGeometry());
        target["offset"] = new H.math.Point(
          pointer.viewportX - targetPosition.x,
          pointer.viewportY - targetPosition.y
        );
        behavior.disable();
      }
    },
    false
  );

  // re-enable the default draggability of the underlying map
  // when dragging has completed
  map.addEventListener(
    "dragend",
    function(ev) {
      var target = ev.target;
      if (target instanceof H.map.Marker) {
        behavior.enable();
      }
    },
    false
  );

  // Listen to the drag event and move the position of the marker
  // as necessary
  map.addEventListener(
    "drag",
    function(ev) {
      var target = ev.target,
        pointer = ev.currentPointer;
      if (target instanceof H.map.Marker) {
        target.setGeometry(
          map.screenToGeo(
            pointer.viewportX - target["offset"].x,
            pointer.viewportY - target["offset"].y
          )
        );
      }
    },
    false
  );
}
export default {
  name: "HereMap",
  data() {
    return {
      map: {},
      platform: {}
    };
  },
  props: {
    appId: String,
    appCode: String,
    lat: String,
    lng: String,
    width: String,
    height: String
  },
  created() {
    var H = window.H;
    this.platform = new H.service.Platform({
      app_id: this.appId,
      app_code: this.appCode
    });
  },
  mounted() {
    var H = window.H;
    var pixelRatio = 2;
    const defaultLayers = this.platform.createDefaultLayers({
      tileSize: 256 * pixelRatio
    });

    this.map = new H.Map(
      this.$refs.map,
      this.platform
        .getMapTileService({
          type: "base"
        })
        .createTileLayer(
          "maptile",
          "reduced.day",
          256 * pixelRatio, // bigger tile size for retina
          "png"
        ),
      {
        center: new H.geo.Point(29, -95),
        zoom: 4,
        style: "default",
        pixelRatio: pixelRatio
      }
    );

    const behavior = new H.mapevents.Behavior(
      new H.mapevents.MapEvents(this.map)
    );
    let ui = H.ui.UI.createDefault(this.map, defaultLayers);
    ui.removeControl("mapsettings");

    var map = this.map;
    getCoordByName("Саратов").then(console.log);
    addCircleMarker("Санкт-Петербург", map, behavior, H);
  }
};
</script>

<style scoped></style>