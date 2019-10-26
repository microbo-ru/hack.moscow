<template>
  <v-app>
    <div v-if="person_info">
      <v-row>
        <v-col>
          <v-card>
            <v-img
              height="600px"
              src="http://www.assembly.spb.ru/images/content/%D0%B4%D0%B5%D0%BF%D1%83%D1%82%D0%B0%D1%82%D1%8B%206%20%D1%81%D0%BE%D0%B7%D1%8B%D0%B2/%D1%80%D0%B0%D1%81%D1%81%D1%83%D0%B4%D0%BE%D0%B2.jpg"
            ></v-img>
            <v-card-title>{{person_info.name}}</v-card-title>
            <v-card-text>В сентябре 2016 г. избран депутатом Законодательного Собрания Санкт-Петербурга 6-го созыва по единому избирательному округу от Санкт-Петербургского городского отделения политической партии "КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ".</v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-container>
            <v-row>
              <v-col v-for="(data, year, index) in person_info.years" :key="index">
                <v-btn
                  :color="year==year_selected ? 'primary' : 'normal' "
                  @click="clicked(year)"
                >{{year}}</v-btn>
              </v-col>
            </v-row>
            <v-row></v-row>
          </v-container>
        </v-col>
      </v-row>
    </div>
  </v-app>
</template>

<script>
//import * as d3 from "d3";
export default {
  name: "SummVis",
  data() {
    return {
      person_info: {},
      year_selected: 2016
    };
  },
  methods: {
    async fetch_data() {
      this.person_info = await fetch("http://localhost:5000/api/nagl", {
        "Content-type": "application/json"
      }).then(res => {
        return res.json();
      });
    },
    clicked(year) {
      this.year_selected = year;
    }
  },
  created() {
    this.fetch_data();
  }
};
</script>

<style >
</style>