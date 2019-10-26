<template>
  <div id="app">
    <HereMap
      appId="lmDfff27MoZlUJmc5ZgX"
      appCode="98vUqPDEgoMgriX_YWU4wA"
      lat="37.7397"
      lng="-121.4252"
      width="100%"
      height="835px"
    />
  </div>
</template>

<script>
import HereMap from "../components/NukeMap.vue";

export default {
  name: "NukeMapView",
  components: {
    HereMap
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>