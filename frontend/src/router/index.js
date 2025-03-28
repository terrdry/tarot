// // src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import CardList from '../components/CardList.vue';
// // // import CardForm from '../components/CardForm.vue';
// // import CardDetail from '../components/CardDetail.vue';
// // import AddCard from '../components/AddCard.vue';

const routes = [
  { path: '/cards', component: CardList }
//   { path: '/card/new', component: AddCard },
//   { path: '/card/:id', component: CardDetail },
// //   { path: '/card/:id/edit', component: CardForm },
];

// vite.config.ts
// import { defineConfig } from 'vite'
// import { createHtmlPlugin } from 'vite-plugin-html'
// import vueDevTools from 'vite-plugin-vue-devtools'

// export default defineConfig({
//   plugins: [
//     // register vueDevTools before createHtmlPlugin
//     vueDevTools()
//     // createHtmlPlugin({})
//   ]
// })

const router = createRouter({
  history: createWebHistory(),
  routes,

});


export default router;

