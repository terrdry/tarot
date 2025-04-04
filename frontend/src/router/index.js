// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import CardList from '@/components/CardList.vue';
import CardDetail from '@/components/CardDetail.vue';
import CardForm from '@/components/CardForm.vue';

import HelloWorld from '@/components/HelloWorld.vue';



const routes = [
  { path: '/', component: HelloWorld, props: { msg: "Goto the Choppers" } },
  // { path: '/:pathMatch(.*)*', redirect: '/' },
  { path: '/cards', component: CardList },
  { path: '/cards/add', component: CardList },
  { path: '/cards/delete/:id', component: CardList },
  { path: '/cards/read/:id', component: CardDetail },
  { path: '/cards/update/:id', component: CardList },
  //   { path: '/card/:id', component: CardDetail },
  { path: '/cards/:id/edit', component: CardForm },
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
  routes: routes,

});


export default router;

