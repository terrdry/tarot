<script setup>
// import api from '../services/api/api'
import tarotDataService from '../services/TarotDataService'
import { ref, onMounted } from 'vue'
// import routes from "../router"

// import { useRoute } from 'vue-router'
// const route = useRoute();

var items = ref([])

const fetchItems = async () => {
  try {
    items.value = await tarotDataService.getAll()
    console.log(items.value)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}
onMounted(fetchItems) // Fetch items when component mounts
</script>

<template>
  <h2>Items</h2>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
  <p> Items:{{ items.data }}</p>
  <div>
    <b-table striped hover :items="items.data"></b-table>
  </div>
  <!-- <ul>
    <li v-for="item in items.data" :key="item.id">
      {{ item.name }} - {{ item.major }} -->
      <!-- <router-link :to="{ name: 'CardDetail', params: { id: item.id } }">Edit</router-link> -->
      <!-- <button @click="deleteItem(item.id)">Delete</button> -->
    <!-- </li>
  </ul>
  <router-link to="cards/add">Add New Item</router-link> -->
</template>
