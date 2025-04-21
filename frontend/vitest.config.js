import { fileURLToPath } from 'url'
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import vueDevTools from 'vite-plugin-vue-devtools'
import cssInjectedByJsPlugin from 'vite-plugin-css-injected-by-js'
import process from 'node:process'

export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    cssInjectedByJsPlugin(),
  ],
  resolve: {
    alias: {
      '@': path.resolve(path.dirname(fileURLToPath(import.meta.url)), 'src'),
      // Removed invalid alias for handling .css files. Use a plugin or loader instead.
    },
  },
  test: {
    globals: true,
    environment: 'jsdom',
    include:['**/components/__tests__/*.spec.js'],
    exclude: ['node_modules', 'dist'],
    coverage: {
      exclude: ['**/node_modules/**', '**/dist/**'],
    },
    setupFiles: path.resolve(
      path.dirname(fileURLToPath(import.meta.url)),
      'src/components/__tests__/setup.js'
    ),
    testTransformMode: {
      web: [/\.css$/],
    },
  },
})
console.log('Test include patterns:', ['**/components/__tests__/*.spec.js']);
console.log('Current working directory:', process.cwd());
console.log('Resolved setupFiles path:', path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  'src/components/__tests__/setup.js'
));
