<template>
  <div id="app">
    <div id="nav">
      <v-tabs>
        <v-tab>
          <router-link to="/">Статистика</router-link>
        </v-tab>
        <v-tab>
          <router-link to="/BivDif">Баттл/Дифф</router-link>
        </v-tab>
        <v-tab>
          <router-link to="/nukemap">Земледелец</router-link>
        </v-tab>
        <v-tab>
          <router-link to="/summvis">Профиль</router-link>
        </v-tab>
        <v-tab>
          <router-link to="/about">О нас</router-link>
        </v-tab>
      </v-tabs>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
