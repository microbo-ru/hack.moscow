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
      // 58550
      this.left = await fetch("http://localhost:5000/api/left/" +
        this.$route.query.left, {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });
      // 58951
      this.right = await fetch("http://localhost:5000/api/right/" +
        this.$route.query.right, {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });
    }
  },
  created() {
    // var t = this.$route.query.test
    // console.log(t);
    // console.log("TT")
    this.fetch_data();
  },
  components: {
    Person
  }
};
</script>

<style >
</style>