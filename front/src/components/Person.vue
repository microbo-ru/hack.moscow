<template>
  <div v-if="data !== undefined">
    <div class="fio">
      {{data.name}} 
      <!-- ({{alignment}}) -->
    </div>
    <hr>
      <!-- {{data.region["name"]}} -->
    <hr>
    <div v-for="(t, idx) of data.years" :key=idx> 
      <hr><hr>
      <div class="year">
        {{idx}}
      </div>
      <hr><hr>
      Доход: {{t.personal_income}}
      <v-img height="64px" width="64px" src="images/rub.png"/>
      <hr>
      Квартиры: {{t.ap_sq}}
      <v-img height="64px" width="64px" src="images/flat.png"/>
      <hr>
      Земля: {{t.land_sq}}
      <v-img height="64px" width="64px" src="images/house.png"/>
    </div>
  </div>
</template>

<style>
  .fio {
    font-weight: bold;
    font-size: 18px;
  }
  .year {
    background-image: linear-gradient(to right top, #051937, #004d7a, #008793, #00bf72, #a8eb12);
  }
</style>


<script>
export default {
  name: "Person",
  props: ["data", "alignment"]
}
</script>