// import './assets/main.css'

// import { createApp } from 'vue'
// import App from './App.vue'
// // import router from './router';

// // createApp(App).use.apply(router).mount('#app')
// createApp(App)

// import Vue from "eslint-plugin-vue";
// const { createApp } = Vue;
import { createApp, ref } from "vue";
import App from "./App.vue"

const app = createApp(App)

// const app = createApp({
//     setup() {
//         const message = ref("Hello, Vue!");

//         const updateMessage = () => {
//             message.value = "You clicked the button!";
//         };

//         return {
//             message,
//             updateMessage
//         };
//     }
// });

app.mount('#app');



