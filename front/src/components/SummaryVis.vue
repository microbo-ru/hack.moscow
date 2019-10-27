<template>
  <v-app width="80%">
    <div v-if="!loading">
      <v-row class="md-6">
        <v-col cols="2"></v-col>
        <v-col>
          <v-card width="400px">
            <v-img
              height="300px"
              width="400px"
              src="http://www.assembly.spb.ru/images/content/%D0%B4%D0%B5%D0%BF%D1%83%D1%82%D0%B0%D1%82%D1%8B%206%20%D1%81%D0%BE%D0%B7%D1%8B%D0%B2/%D1%80%D0%B0%D1%81%D1%81%D1%83%D0%B4%D0%BE%D0%B2.jpg"
            ></v-img>
            <v-card-title style="display:block">{{person_info.name}}</v-card-title>
            <v-card-text>В сентябре 2016 г. избран депутатом Законодательного Собрания Санкт-Петербурга 6-го созыва по единому избирательному округу от Санкт-Петербургского городского отделения политической партии "КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ".</v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-container>
            <v-row>
              <v-container>
                <v-timeline>
                  <v-timeline-item>
                    <template v-slot:opposite>
                      <span v-text="2016"></span>
                    </template>
                    <v-row>
                      <div class="oneline">
                        Доход:
                        <div class="inc">{{numberWithSpaces(timeline_data[2016]["inc"])}}</div>
                      </div>
                    </v-row>
                    <v-row>
                      <div class="oneline">
                        Владеет площадью в
                        <div class="inc">{{numberWithSpaces(timeline_data[2016]["ar"])}}</div>м
                        <sup>2</sup>
                      </div>
                    </v-row>
                    <v-row>
                      <div class="oneline">
                        Является владельцем
                        <div class="inc">{{numberWithSpaces(timeline_data[2016]["veh"])}}</div>машин
                      </div>
                    </v-row>
                  </v-timeline-item>
                  <v-timeline-item>
                    <template v-slot:opposite>
                      <span v-text="2017"></span>
                    </template>
                    <template>
                      <v-row>
                        <div class="oneline">
                          Доход увеличился на:
                          <div class="inc">{{numberWithSpaces(timeline_data[2017]["inc"])}}</div>
                        </div>
                      </v-row>
                      <v-row>
                        <div class="oneline">
                          Потерял
                          <div class="dec">{{numberWithSpaces(timeline_data[2017]["ar"])}}</div>м
                          <sup>2</sup> земли
                        </div>
                      </v-row>
                      <v-row>
                        <div class="oneline">количество машин не изменилось</div>
                      </v-row>
                    </template>
                  </v-timeline-item>
                  <v-timeline-item>
                    <template v-slot:opposite>
                      <span v-text="2018"></span>
                    </template>
                    <v-row>
                      <div class="oneline">
                        Доход уменьшился на:
                        <div class="dec">{{numberWithSpaces(timeline_data[2018]["inc"])}}</div>
                      </div>
                    </v-row>
                    <v-row>
                      <div class="oneline">
                        Потерял
                        <div class="dec">{{numberWithSpaces(timeline_data[2018]["ar"])}}</div>м
                        <sup>2</sup> земли
                      </div>
                    </v-row>
                    <v-row>
                      <div class="oneline">количество машин не изменилось</div>
                    </v-row>
                  </v-timeline-item>
                </v-timeline>
              </v-container>
            </v-row>
          </v-container>
        </v-col>
        <v-col cols="2"></v-col>
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
      year_selected: 2016,
      timeline_data: {},
      loading: true
    };
  },
  methods: {
    async fetch_data() {
      await fetch("http://localhost:5000/api/nagl", {
        "Content-type": "application/json"
      })
        .then(res => {
          return res.json();
        })
        .then(res => {
          this.person_info = res;
          this.clalc_timeline_data();
        });
    },
    clicked(year) {
      this.year_selected = year;
    },
    clalc_timeline_data() {
      let py = this.person_info["years"];
      this.timeline_data[2016] = {
        inc: py[2016]["personal_income"] | 0,
        ar: py[2016]["personal_sq"] | 0,
        veh: py[2016]["personal_veh"] | 0
      };
      this.timeline_data[2017] = {
        inc: (py[2017]["personal_income"] - py[2016]["personal_income"]) | 0,
        ar: (py[2017]["personal_sq"] - py[2016]["personal_sq"]) | 0,
        veh: (py[2017]["personal_vel"] - py[2016]["personal_veh"]) | 0
      };
      this.timeline_data[2018] = {
        inc: (py[2018]["personal_income"] - py[2017]["personal_income"]) | 0,
        ar: (py[2018]["personal_sq"] - py[2017]["personal_sq"]) | 0,
        veh: (py[2018]["personal_veh"] - py[2017]["personal_veh"]) | 0
      };
      this.loading = false;
    },
    numberWithSpaces(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    }
  },
  created() {
    this.fetch_data();
  }
};
</script>

<style >
.inc {
  color: green;
}

.dec {
  color: lightcoral;
}

h5 {
  font-size: 0.3rem;
}

.oneline {
  overflow: hidden;
  white-space: nowrap;
  font-size: 1rem;
  width: 100%;
  display: flex;
}
</style>