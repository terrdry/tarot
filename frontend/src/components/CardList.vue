
<template>
  <h2>Items</h2>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.name }} - {{ item.description }}
      <router-link :to="{ name: 'ItemEdit', params: { id: item.id } }">Edit</router-link>
      <button @click="deleteItem(item.id)">Delete</button>
    </li>
  </ul>
  <router-link to="/create">Add New Item</router-link>
</template>

<script>
// import api from '../services/api'
import api from '../services/api/cardService.js';

export default {
  data() {
    return {
      items: [],
    }
  },
  mounted() {
    this.fetchItems()
  },
  methods: {
    async fetchItems() {
      const response = await api.get('/items')
      this.items = response.data
    },
    async deleteItem(id) {
      await api.delete(`/items/${id}`)
      this.fetchItems()
    },
  },
}
</script>
