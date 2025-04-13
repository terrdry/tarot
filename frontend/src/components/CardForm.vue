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
          v-model="radioAttrib"
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
          <b-button pill @click="addModCard(curentTarot)" variant="success" target="_blank">
            SAVE
          </b-button>
          <b-button pill @click="goBack" variant="warning" target="_blank"> CANCEL </b-button>
        </b-button-group>
      </div>
    </form>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Tarot...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import TarotDataService from '../services/api/TarotDataService'

const route = useRoute()
const router = useRouter()
const cardId = route.params.id

const currentTarot = ref({})
const radioAttrib = ref({})

const fetchItems = async () => {
  try {
    const response = await TarotDataService.get(parseInt(cardId))
    currentTarot.value = response.data
    console.log(response.data)
  } catch (e) {
    console.log('fetchItems ' + e)
  }
}
const addModCard = async () => {
  try {
    if (route.params.id != 0) {
      const response = await TarotDataService.update(parseInt(cardId), currentTarot.value)
      currentTarot.value = response.data
      console.log(currentTarot.value)
    } else {
      console.log(currentTarot.value)
      const response = await TarotDataService.create(currentTarot.value)
      currentTarot.value = response.data
      goBack()
    }
  } catch (error) {
    console.log('addModCard ' + error)
  }
}
const goBack = () => {
  router.back()
  console.log('hello')
}

onMounted(() => {
  if (cardId != 0) {
    fetchItems()
  } else {
    currentTarot.value = {
      id: 0,
      name: '',
      major: false,
    }
  }
})
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>
