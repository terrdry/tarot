<script setup>
// import cardService from '@/services/api/cardService'

import { BButton } from 'bootstrap-vue-3'
import tarotDataService from '../services/TarotDataService'
import { ref, onMounted } from 'vue'
// import routes from "../router"

// import { useRoute } from 'vue-router'
// const route = useRoute();

var items = ref([])
var fields = ['id', 'name', 'link']



const goTo = (id, action) => {
  console.log(id)
  console.log(action)
}

const fetchItems = async () => {
  try {
    items.value = await tarotDataService.getAll()
    console.log(items.value)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}

// const addCard = () => {
//   try {
//     console.log('here')
//     const record_to_add = { name: 'The Magician', isMajor: 'True', img: 'TODO.TXT' }
//     items.value = tarotDataService.post(record_to_add)
//   } catch (error) {
//     console.log(error)
//   }
// }

// const deleteItem = (items)
onMounted(fetchItems) // Fetch items when component mounts
</script>

<template>
  <h2>Items</h2>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
  <!-- <p> Items:{{ items.data }}</p> -->
  <div>
    <b-table striped hover :items="items.data" :fields="fields">
      <template #cell(link)="data">
        <b-button-group>
          <b-button
            pill
            :to="{ name: 'CardDetail',
                  // props: {default: true },
                  params: { id: 1 } }"
            variant="outline-success"
            target="_blank"
          >
            EDIT
          </b-button>
          <b-button
            pill
            variant="outline-danger"
            @click="goTo(data.id, 'delete')"
            target="_blank"
          >
            DELETE
          </b-button>
        </b-button-group>
      </template>
    </b-table>
  </div>
  <!-- <ul>
    <li v-for="item in items.data" :key="item.id">
      {{ item.name }} - {{ item.major }} -->
  <!-- <router-link :to="{ name: 'CardDetail', params: { id: item.id } }">Edit</router-link> -->
  <!-- <button @click="deleteItem(item.id)">Delete</button> -->
  <!-- </li>
        </ul> -->
  <b-button pill variant="outline-primary" target="_blank"> EDIT </b-button>
</template>
