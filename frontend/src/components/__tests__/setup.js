// import { beforeEach } from 'vitest'
// import { config } from 'vitest'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { createRouter, createWebHistory } from 'vue-router'
import 'vuetify/styles'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

import path from 'path'
import { fileURLToPath } from 'url'
import process from 'process'


const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
})

// If you have real routes, import and use them
const router = createRouter({
    history: createWebHistory(),
    // Add your routes here. Example:
    // { path: '/example', component: ExampleComponent }
    routes: [],

})
console.log('Current working directory:', process.cwd());
console.log('Resolved setupFiles path:', path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  'src/components/__tests__/setup.js'
));
// Inject Vuetify and Router into Vue Test Utils global config
// This ensures that all components tested have access to Vuetify's UI components and styles,
// as well as the Vue Router instance for navigation-related functionality.
// It simplifies testing by providing these plugins globally, avoiding the need to configure them in each test.
// Inject globally before each test
// beforeEach(() => {
//     config.global.plugins = [vuetify, router]
//   })

// config.plugins = [vuetify, router];
export default [vuetify, router]
