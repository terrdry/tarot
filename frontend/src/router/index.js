/**
 * Vue Router configuration for the Tarot application.
 *
 * This file sets up the routes for the application using Vue Router.
 * Each route is associated with a specific component and path.
 *
 * Routes:
 * - `/cards`: Displays the `CardList` component.
 * - `/cards/add`: Displays the `CardForm` component for adding a new card. Named route: `cardForm`.
 * - `/cards/delete/:id`: Displays the `CardList` component for deleting a card by ID.
 * - `/cards/read/:id`: Displays the `CardForm` component for reading a card by ID. Named route: `cardForm`.
 * - `/cards/update/:id`: Displays the `CardList` component for updating a card by ID.
 * - `/`: Displays the `HelloWorld` component with a custom message passed as a prop.
 *
 * The router uses HTML5 history mode for navigation.
 *
 * @module router/index
 * @requires vue-router
 * @requires @/components/CardList.vue
 * @requires @/components/HelloWorld.vue
 */
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import CardList from '@/components/CardList.vue';
import HelloWorld from '@/components/HelloWorld.vue';

const routes = [
  { path: '/cards', component: CardList },
  { path: '/cards/delete/:id', component: CardList },
  { path: '/cards/update/:id', component: CardList },
  { path: '/', component: HelloWorld, props: { msg: "Welcome" } },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
