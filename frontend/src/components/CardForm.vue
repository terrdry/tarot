<template>
  <div v-if="currentTarot" class="edit-form">
    <h4>Tarot</h4>
    <form @submit.prevent>
      <div>
        <b-form-group description="Tarot Card name." label="Name" label-for="tarot-name">
          <b-form-input id="name" v-model="currentTarot.name"> </b-form-input>
        </b-form-group>
      </div>
      <div>
        <b-form-checkbox
          id="checkbox-1"
          v-model="stat"
          name="checkbox-1"
          value="accepted"
          switch="true"
          unchecked-value="not_accepted"
        >
          Major Arcana
        </b-form-checkbox>
      </div>
      <div>
        <b-button-group>
          <b-button
            pill
            variant="success"
            target="_blank"
          >
            SAVE
          </b-button>
          <b-button
            pill
            variant="warning"
            target="_blank"
          >
            CANCEL
          </b-button>
        </b-button-group>
      </div>
    </form>
    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Tarot...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import TarotDataService from '../services/TarotDataService'

const route = useRoute()
const router = useRouter()

const currentTarot = ref(null)
const message = ref('')
const stat = ref({})

const getTarot = async (id) => {
  try {
    const response = await TarotDataService.get(id)
    currentTarot.value = response.data
    console.log(response.data)
  } catch (e) {
    console.log(e)
  }
}

// const updatePublished = async (status) => {
//   try {
//     const data = {
//       id: currentTarot.value.id,
//       title: currentTarot.value.title,
//       description: currentTarot.value.description,
//       published: status,
//     }

//     const response = await TarotDataService.update(currentTarot.value.id, data)
//     console.log(response.data)
//     currentTarot.value.published = status
//     message.value = 'The status was updated successfully!'
//   } catch (e) {
//     console.log(e)
//   }
// }

const updateTarot = async () => {
  try {
    const response = await TarotDataService.update(currentTarot.value.id, currentTarot.value)
    console.log(response.data)
    message.value = 'The tarot was updated successfully!'
  } catch (e) {
    console.log(e)
  }
}

// const deleteTarot = async () => {
//   try {
//     const response = await TarotDataService.delete(currentTarot.value.id)
//     console.log(response.data)
//     router.push({ name: 'tutorials' })
//   } catch (e) {
//     console.log(e)
//   }
// }

onMounted(() => {
  message.value = 'The stars my destination'
  getTarot(route.params.id)
  console.log('hello')
})
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
