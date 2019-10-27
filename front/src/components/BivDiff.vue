<template>
  <v-row>
    <v-col>
      <person :data="left" alignment="right"/>
    </v-col>
    <v-col>
      <person :data="right" alignment="left"/>
    </v-col>
  </v-row>
</template>

<script>
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
      this.left = await fetch("http://localhost:5000/api/left/58550", {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });

      this.right = await fetch("http://localhost:5000/api/right/58951", {
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