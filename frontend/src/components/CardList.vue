<script setup>
// import cardService from '@/services/api/cardService'

import tarotDataService from '../services/TarotDataService'
import { ref, onMounted } from 'vue'
// import routes from "../router"

// import { useRoute } from 'vue-router'
// const route = useRoute();

var items = ref([{ name: 'hussein', id: 1, isMajor: 'True' }])

const fetchItems = async () => {
  try {
    items.value = await tarotDataService.getAll()
    console.log(items)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}

const addCard = () => {
  try {
    console.log('here')
    const record_to_add = { 'name': "The Magician", 'isMajor': 'True' , 'img':'TODO.TXT'}
    items.value = tarotDataService.post(record_to_add)
  } catch (error) {
    console.log(error)
  }
}

// const deleteItem = (items)
onMounted(fetchItems) // Fetch items when component mounts
</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tarot Cards</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" @click="addCard">Add Card</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Card Name</th>
              <th scope="col">Major Arcana</th>
              <th scope="col">Image</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items.data" :key="item.id">
              <td>{{ item.name }}</td>
              <td>
                <span v-if="item.major">Yes</span>
                <span v-else>No</span>
              </td>
              <td>{{ item.img }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
