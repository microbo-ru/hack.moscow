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
        <div class="income">Доход: {{t.personal_income}}</div>
        <div class="income">
          <v-img  height="64px" width="64px" src="images/rub.png"/>
        </div>
      <hr>
        <div class="income">Квартиры: {{Number(t.ap_sq).toFixed(2)}} м<sup>2</sup></div>
        <div class="income">
          <v-img height="64px" width="64px" src="images/flat.png"/>
        </div>
      <hr>
        <div class="income">Земля: {{t.land_sq}} м<sup>2</sup></div>
        <div class="income">
          <v-img height="64px" width="64px" src="images/house.png"/>
        </div>
    </div>
  </div>
</template>

<style>
  .fio {
    font-weight: bold;
    font-size: 18px;
  }
  .income {
    display: inline-block;
    vertical-align: middle;
    margin: 10px;
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