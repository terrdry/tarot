<template>
    <v-btn color="primary" @click="clicked = true">
      Click me
    </v-btn>
  </template>

  <script setup>
  import { ref } from 'vue'
  const clicked = ref(false)
  </script>
