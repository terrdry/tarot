// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import CardList from '@/components/CardList.vue';
import CardForm from '@/components/CardForm.vue';
import HelloWorld from '@/components/HelloWorld.vue';



const routes = [
  { path: '/cards', component: CardList },
  { path: '/cards/add', component: CardForm, name: 'cardForm' },
  { path: '/cards/delete/:id', component: CardList },
  { path: '/cards/read/:id', component: CardForm, name: 'cardForm' },
  { path: '/cards/update/:id', component: CardList },
  { path: '/', component: HelloWorld, props: { msg: "Goto the Choppers" } },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});


export default router;
