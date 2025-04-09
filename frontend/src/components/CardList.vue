<script setup>
import { BButton } from 'bootstrap-vue-3'
import tarotDataService from '../services/TarotDataService'
import { ref, onMounted } from 'vue'

// import routes from "../router"
import { useRoute } from 'vue-router'
const route = useRoute()

var items = ref([])
var fields = ['id', 'name', 'link']
// const route = useRoute()

// const goTo = (id, action) => {
//   console.log(id)
//   console.log(action)
// }

const fetchItems = async () => {
  try {
    const response = await tarotDataService.getAll()
    items.value = response.data
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
  <h2>Tarot Cards</h2>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
  <!-- <p> Items:{{ items }}</p> -->

  <div>
    <b-table striped hover :items="items" :fields="fields">
      <template #cell(link)="tarot_card">
        <b-button-group>
          <!-- <p>{{ tarot_card.item.id }}</p> -->
          <b-button
            pill
            :to="{ name: 'cardForm',
                  params: { id: tarot_card.item.id } }"
            variant="outline-success"
          >
            EDIT
          </b-button>
          <b-button pill variant="outline-danger" target="_blank"> DELETE </b-button>
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
