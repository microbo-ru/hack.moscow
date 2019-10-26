import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import NukeMapView from "../views/NukeMapView.vue";
import summvis from "../views/SummVisView.vue";
import bivdif from "../views/BivDifView.vue";
import about from "../views/AboutView.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },

  {
    path: "/nukemap",
    name: "nukemap",
    component: NukeMapView
  },
  {
    path: "/summvis",
    name: "sumvis",
    component: summvis
  },
  {
    path: "/BivDif",
    name: "bivdif",
    component: bivdif
  },
  {
    path: "/about",
    name: "about",
    component: about
  }
];

const router = new VueRouter({
  routes
});

export default router;
