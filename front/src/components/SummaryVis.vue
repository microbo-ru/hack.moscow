<template>
  <div>{{person_info}}</div>
</template>

<script>
//import * as d3 from "d3";
export default {
  name: "SummVis",
  data() {
    return {
      person_info: {}
    };
  },
  methods: {
    async fetch_data() {
      this.person_info = await fetch("http://localhost:5000/api/nagl", {
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