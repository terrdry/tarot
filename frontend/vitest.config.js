import { fileURLToPath } from 'url'
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [
    vue(),
    ],
  build: {
    sourcemap: true
  },
  resolve: {
    alias: {
      '@': path.resolve(path.dirname(fileURLToPath(import.meta.url)), 'src'),
      '\\.css$': path.resolve(path.dirname(fileURLToPath(import.meta.url)), 'src/components/__tests__/styleStub.js'),
    },
  },
  test: {
    setupFiles: path.resolve(
      path.dirname(fileURLToPath(import.meta.url)),
      'src/components/__tests__/setup.js'
    ),
    globals: true,
    environment: 'jsdom',
    // server: {
    //   deps: {
    //     inline: ['vuetify'],
    //   },
    // },
    deps: {
      inline: ['vuetify'],
    },
    include: ['**/components/__tests__/*.spec.js'],
    exclude: ['node_modules', 'dist'],
    coverage: {
      exclude: ['**/node_modules/**', '**/dist/**'],
    },
  }
});
