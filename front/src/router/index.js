import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import NukeMapView from "../views/NukeMapView.vue";
import summvis from "../views/SummVisView.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
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
  }
];

const router = new VueRouter({
  routes
});

export default router;
