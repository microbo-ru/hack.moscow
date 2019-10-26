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
        return json.response.GeoObjectCollection.featureMember[0].GeoObject
          .Point;
      });
    }
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
    console.log(behavior);

    var circle = new H.map.Circle({ lat: 52.51, lng: 13.4 }, 8000);
    this.map.addObject(circle);

    getCoordByName("Челябинск").then(console.log);
  }
};
</script>

<style scoped></style>