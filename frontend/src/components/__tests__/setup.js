/**
 * Sets up global configurations for Vue Test Utils and provides necessary
 * plugins and mocks for testing Vue components with Vuetify and Vue Router.
 *
 * Features:
 * - Configures a Vuetify instance with components, directives, and Material Design Icons (MDI).
 * - Creates a dummy Vue Router instance with a basic route for testing purposes.
 * - Applies the Vuetify and Router plugins globally before all tests.
 * - Mocks the `ResizeObserver` class to address compatibility issues with JSDOM.
 *
 * Dependencies:
 * - `@vue/test-utils` for configuring global plugins.
 * - `vuetify` for UI components and styling.
 * - `vue-router` for routing functionality.
 * - `vitest` for test lifecycle hooks.
 *
 * Notes:
 * - The `ResizeObserver` mock is a workaround for compatibility issues in JSDOM.
 * - The `beforeAll` lifecycle hook ensures the plugins are applied before any tests run.
 */
import { beforeAll } from 'vitest'
import { createVuetify } from 'vuetify'
import { createRouter, createWebHistory } from 'vue-router'
import { config } from '@vue/test-utils'
import 'vuetify/styles'
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { aliases, mdi } from 'vuetify/iconsets/mdi'

// Create Vuetify instance
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

// create a dummy router
const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: {template: '<div />'} },
    ],
})

beforeAll(() => {
    config.global.plugins = [ vuetify, router ]
});

// Mock ResizeObserverclass
class ResizeObserver {
    observe() {}
    unobserve() {}
    disconnect() {}
  }
  // This is a workaround for the ResizeObserver issue in JSDOM
  globalThis.ResizeObserver = ResizeObserver;
