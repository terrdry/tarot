<script setup>
import { BButton } from 'bootstrap-vue-3'
import TarotDataService from '../services/api/TarotDataService'
import { ref, onMounted } from 'vue'

// import routes from "../router"
import { useRouter } from 'vue-router'

var items = ref([])
var fields = ['id', 'name', 'link']
// const router = useRouter()

const fetchItems = async () => {
  try {
    const response = await TarotDataService.getAll()
    items.value = response.data
    console.log(items.value)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}

const deleteTarot = async (id) => {
  try {
    const response = await TarotDataService.delete(id)
    console.log(response.data)
    // router.go()
  } catch (e) {
    console.log(e)
  }
}
onMounted(fetchItems) // Fetch items when component mounts
</script>


<template>
  <h2>Tarot Cards</h2>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>

  <div>
    <b-table striped hover :items="items" :fields="fields">
      <template #cell(link)="tarot_card">
        <b-button-group>
          <b-button
            pill
            :to="{ name: 'cardForm', params: { id: tarot_card.item.id } }"
            variant="outline-success"
          >
            EDIT
          </b-button>
          <b-button pill variant="outline-danger" @click="deleteTarot(tarot_card.item.id)">
            DELETE
          </b-button>
        </b-button-group>
      </template>
    </b-table>
  </div>
  <b-button pill variant="outline-primary" :to="{ name: 'cardForm', params: { id: 0 } }">
    ADD
  </b-button>
</template>
