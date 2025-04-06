<script setup>
import { ref } from 'vue'
import TarotDataService from '../services/TarotDataService'

// Reactive state
const tarot_card = ref({
  id: null,
  name: '',
  major: '',
  img: 'TODO.txt',
})

const submitted = ref(false)

// Save card function
const saveCard = () => {
  const data = {
    name: tarot_card.value.name,
    isMajor: tarot_card.value.value,
  }

  TarotDataService.create(data)
    .then((response) => {
      tarot_card.value.id = response.data.id
      console.log(response.data)
      submitted.value = true
    })
    .catch((error) => {
      console.log(error)
    })
}

// Reset form
const newCard = () => {
  submitted.value = false
  tarot_card.value = {
    id: null,
    name: '',
    major: 'False',
    published: false,
  }
}
</script>

<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="name">name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          required
          v-model="tarot_card.name"
          name="name"
        />
      </div>

      <div class="form-group">
        <label for="major">Major Arcana</label>
        <input
          class="form-control"
          id="major"
          required
          v-model="tarot_card.major"
          name="major"
        />
      </div>

      <button @click="savecard" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newCard">Add</button>
    </div>
  </div>
</template>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>
