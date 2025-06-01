import { createRouter, createWebHistory } from "vue-router";
import GetStarted from "../pages/GetStarted.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/Dashboard.vue";

const routes = [
  {
    path: "/",
    name: "GetStarted",
    component: GetStarted,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
