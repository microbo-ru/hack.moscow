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
  });
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
        center: new H.geo.Point(60, 51),
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