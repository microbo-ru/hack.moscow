<template>
  <div>
    {{data.name}} ({{alignment}})
    <hr>
    {{data.region["name"]}}
    <hr>
    <div v-for="(t, idx) of data.years" :key=idx> 
      <hr><hr>
      {{idx}}
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

<script>
export default {
  name: "Person",
  props: ["data", "alignment"]
}
</script>