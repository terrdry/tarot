// import './assets/main.css'

// import { createApp } from 'vue'
// import App from './App.vue'
// // import router from './router';

// // createApp(App).use.apply(router).mount('#app')
// createApp(App)

// import Vue from "eslint-plugin-vue";
// const { createApp } = Vue;
import { createApp } from "vue";
import App from "./App.vue"
import router from "./router"

const app = createApp(App)
app.use(router)

app.mount("#app")
