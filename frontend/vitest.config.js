import { fileURLToPath } from 'url'
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import path from 'path'
// import vueDevTools from 'vite-plugin-vue-devtools'
// import cssInjectedByJsPlugin from 'vite-plugin-css-injected-by-js'
import { patchCssModules } from 'vite-css-modules'
import process from 'node:process'


export default defineConfig({
  plugins: [
    vue(),
    // vueDevTools(),
    // cssInjectedByJsPlugin(),
    patchCssModules(),
    // ignore( ['**/*.css']),
  ],
  resolve: {
    alias: {
      '@': path.resolve(path.dirname(fileURLToPath(import.meta.url)), 'src'),
      '\\.css$': path.resolve(path.dirname(fileURLToPath(import.meta.url)), 'src/components/__tests__/styleStub.js'),
    },
  },
  test: {
    globals: true,
    environment: 'jsdom',
    transformMode: {
      web: [/\.css$/],
    },
    server: {
      deps: {
        inline: ['vuetify'],
      },
    },

    include: ['**/components/__tests__/*.spec.js'],
    exclude: ['node_modules', 'dist'],
    coverage: {
      exclude: ['**/node_modules/**', '**/dist/**'],
    },
    css: true,
    setupFiles: path.resolve(
      path.dirname(fileURLToPath(import.meta.url)),
      'src/components/__tests__/setup.js'
    ),
  },
  build: {
    target: 'es2022',
  },
})

// console.log('Test include patterns:', default)
console.log('Current working directory:', process.cwd());
console.log('Resolved setupFiles path:', path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  'src/components/__tests__/setup.js'
));
