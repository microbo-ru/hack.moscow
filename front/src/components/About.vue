<template>
  <div>{{summ}}</div>
</template>

<script>
//import * as d3 from "d3";
export default {
  name: "About",
  data() {
    return {
      summ: {}
    };
  },
  methods: {
    async fetch_data() {
      this.summ = await fetch("http://localhost:5000/api/map", {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });
    }
  },
  created() {
    this.fetch_data();
  }
};
</script>

<style >
</style>