import { createRouter, createWebHistory } from "vue-router";
import GetStarted from "../pages/GetStarted.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/Dashboard.vue";
import CreateMahasiswa from "../pages/AksiCRUD/CreateMahasiswa.vue";
import ReadMahasiswa from "../pages/AksiCRUD/ReadMahasiswa.vue";
import UpdateMahasiswa from "../pages/AksiCRUD/UpdateMahasiswa.vue";
import DeleteMahasiswa from "../pages/AksiCRUD/DeleteMahasiswa.vue";

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
  {
    path: "/dashboard/create",
    name: "CreateMahasiswa",
    component: CreateMahasiswa,
  },
  {
    path: "/dashboard/read",
    name: "ReadMahasiswa",
    component: ReadMahasiswa,
  },
  {
    path: "/dashboard/update",
    name: "UpdateMahasiswa",
    component: UpdateMahasiswa,
  },
  {
    path: "/dashboard/delete",
    name: "DeleteMahasiswa",
    component: DeleteMahasiswa,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
