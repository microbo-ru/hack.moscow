<template>
  <v-row>
    <v-col>
      <!-- {{left}} -->
      <person :data="left"/>
    </v-col>
    <v-col>
      <!-- {{right}} -->
      <person :data="right"/>
    </v-col>
  </v-row>
</template>

<script>
//import * as d3 from "d3";
import Person from "../components/Person";

export default {
  name: "BivDif",
  data() {
    return {
      left: {},
      right: {}
    };
  },
  methods: {
    async fetch_data() {
      this.left = await fetch("http://localhost:5000/api/left", {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });

      this.right = await fetch("http://localhost:5000/api/right", {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });
    }
  },
  created() {
    this.fetch_data();
  },
  components: {
    Person
  }
};
</script>

<style >
</style>