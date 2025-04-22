<template>
    <v-btn color="primary" @click="clicked = true">
      Click me
    </v-btn>
  </template>

  <script setup>
  /**
   * A reactive reference `clicked` is defined using Vue's `ref` function.
   * It is initialized to `false` and can be used to track the state of a button click
   * or any other boolean-based interaction within the component.
   */
  import { ref } from 'vue'
  const clicked = ref(false)
  </script>
