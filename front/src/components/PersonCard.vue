<template>
  <v-app>
    <v-card>
      <v-img height="600px" :src="src"></v-img>
      <v-card-title>{{name}}</v-card-title>
      <v-card-text>{{description}}</v-card-text>
    </v-card>
  </v-app>
</template>

<script>
export default { name: "PersonCard", props: ["src", "name", "description"] };
</script>