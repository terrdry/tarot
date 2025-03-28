
<template>
  <h2>Items</h2>
  <p> {{ items.data }}</p>
  <ul>
    <li v-for="item in items.data" :key="item.id">
      {{ item.name }} - {{ item.major }}
      <!-- {{ item.name }} - {{ item.description }} -->
      <!-- {{ item[0] }} -->
      <!-- <router-link :to="{ name: 'ItemEdit', params: { id: item.id } }">Edit</router-link> -->
      <!-- <button @click="deleteItem(item.id)">Delete</button> -->
    </li>
  </ul>
  <!-- <router-link to="/create">Add New Item</router-link> -->
  <h2>Delete</h2>
</template>

<script>
// import api from '../services/api/api'
import tarotDataService from "../services/TarotDataService"
import { ref, onMounted } from "vue"

export default {
  setup() {
    // const items = ref([{ name: "Opposition","description": "what a movie!!", id: 1 }]);
    const items = ref([]);


    const fetchItems = async () => {
      try {

        items.value = await tarotDataService.getAll();
        console.log(items)

      } catch (error) {
        console.error("Error fetching items:", error);
      }
    };

    // const deleteItem = async (id) => {
    //   try {
    //     await api.delete(`/items/${id}`);
    //     fetchItems(); // Refresh list after deletion
    //   } catch (error) {
    //     console.error("Error deleting item:", error);
    //   }
    // };

    onMounted(fetchItems()); // Fetch items when component mounts

    return {
      items
      // deleteItem,
    };
  },
};
</script>
