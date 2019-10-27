<template>
  <div class="here-map">
    <div ref="map" v-bind:style="{ width: width, height: height }"></div>
  </div>
</template>

<script>
// function getCoordByName(name) {
//   return fetch(
//     `https://geocode-maps.yandex.ru/1.x/?apikey=2d121788-cbff-41a5-9cfb-62e349951e8b&format=json&geocode=${name}`
//   ).then(response => {
//     if (response.ok) {
//       return response.json().then(json => {
//         console.log(json);
//         return json.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos
//           .split(" ")
//           .map(parseFloat);
//       });
//     }
//   });
// }

// function addCircleMarker(name, map, behavior, H) {
//   getCoordByName(name).then(function(res) {
//     console.log(res);
//     var circle = new H.map.Circle({ lat: res[1], lng: res[0] }, 8000);
//     map.addObject(circle);
//   });
// }

export default {
  name: "HereMap",
  data() {
    return {
      persons: {},
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
  methods: {
    async fetch_data(map, behavior, H) {
      this.persons = await fetch("http://localhost:5000/api/map", {
        "Content-type": "application/json"
      }).then(res => {
        res.json().then(res => {
          let sqa = res[0]["years"][2016]["total_sq"];
          let sqb = res[1]["years"][2018]["total_sq"];
          let sqfama = 52072785.99999999;
          console.log(sqa, sqb);
          let ra = Math.sqrt(sqa / Math.PI);
          let rb = Math.sqrt(sqb / Math.PI);
          let rfama = Math.sqrt(sqfama / Math.PI);
          console.log(ra, rb);
          var circle = new H.map.Circle({ lat: 59.944844, lng: 30.246036 }, ra);
          map.addObject(circle);
          var circle2 = new H.map.Circle(
            { lat: 59.924138, lng: 30.351958 },
            rb,
            {
              style: {
                fillColor: "rgba(0, 255, 24, 0.2)" // Color of the circle
              }
            }
          );
          map.addObject(circle2);
          var circle3 = new H.map.Circle(
            { lat: 59.892215, lng: 30.321622 },
            rfama,
            {
              style: {
                fillColor: "rgba(250, 255, 24, 0.2)" // Color of the circle
              }
            }
          );
          map.addObject(circle3);
          console.log(sqa, sqb);
        });
        // return res.json();
      });
    }
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
        center: new H.geo.Point(59.928761, 30.310878),
        zoom: 11,
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
    // addCircleMarker("Санкт-Петербург", map, behavior, H);
    this.fetch_data(map, behavior, H);
  }
};
</script>

<style scoped></style>