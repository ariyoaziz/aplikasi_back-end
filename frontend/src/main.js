import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";

// Import Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css";

const app = createApp(App);

// PASANG router ke app
app.use(router);

// Mount app ke #app
app.mount("#app");
