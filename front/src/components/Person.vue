<template>
  <div v-if="data !== undefined">
    <div class="fio">
      {{data.name}} 
      <!-- ({{alignment}}) -->
    </div>
    <div v-for="(t, idx) of data.years" :key=idx> 
      <hr>
      <div class="year">
        {{idx}}
      </div>
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
    font: 20pt sans-serif;
    padding-bottom: 15px;
  }
  .income {
    display: inline-block;
    vertical-align: middle;
    margin: 10px;
    font: 16pt sans-serif;
  }
  .year {
    padding: 5px;
    font: 16pt sans-serif;
    font-weight: bold;
    background: rgba(242,246,248,1);
background: -moz-linear-gradient(top, rgba(242,246,248,1) 0%, rgba(216,225,231,0.88) 50%, rgba(181,198,208,0.87) 51%, rgba(224,239,249,0.75) 100%);
background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(242,246,248,1)), color-stop(50%, rgba(216,225,231,0.88)), color-stop(51%, rgba(181,198,208,0.87)), color-stop(100%, rgba(224,239,249,0.75)));
background: -webkit-linear-gradient(top, rgba(242,246,248,1) 0%, rgba(216,225,231,0.88) 50%, rgba(181,198,208,0.87) 51%, rgba(224,239,249,0.75) 100%);
background: -o-linear-gradient(top, rgba(242,246,248,1) 0%, rgba(216,225,231,0.88) 50%, rgba(181,198,208,0.87) 51%, rgba(224,239,249,0.75) 100%);
background: -ms-linear-gradient(top, rgba(242,246,248,1) 0%, rgba(216,225,231,0.88) 50%, rgba(181,198,208,0.87) 51%, rgba(224,239,249,0.75) 100%);
background: linear-gradient(to bottom, rgba(242,246,248,1) 0%, rgba(216,225,231,0.88) 50%, rgba(181,198,208,0.87) 51%, rgba(224,239,249,0.75) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f2f6f8', endColorstr='#e0eff9', GradientType=0 );
  }
</style>


<script>
export default {
  name: "Person",
  props: ["data", "alignment"]
}
</script>