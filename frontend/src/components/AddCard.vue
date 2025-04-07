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
          <label for="title">Title</label>
          <input
            type="text"
            class="form-control"
            id="title"
            required
            v-model="tarot.title"
            name="title"
          />
        </div>

        <div class="form-group">
          <label for="description">Description</label>
          <input
            class="form-control"
            id="description"
            required
            v-model="tarot.description"
            name="description"
          />
        </div>

        <button @click="saveTarot" class="btn btn-success">Submit</button>
      </div>

      <div v-else>
        <h4>You submitted successfully!</h4>
        <button class="btn btn-success" @click="newTarot">Add</button>
      </div>
    </div>
  </template>

  <script>
  import TarotDataService from "../services/TarotDataService";

  export default {
    name: "add-tarot",
    data() {
      return {
        tutorial: {
          id: null,
          title: "",
          description: "",
          published: false
        },
        submitted: false
      };
    },
    methods: {
      saveTarot() {
        var data = {
          title: this.tutorial.title,
          description: this.tutorial.description
        };

        TarotDataService.create(data)
          .then(response => {
            this.tutorial.id = response.data.id;
            console.log(response.data);
            this.submitted = true;
          })
          .catch(e => {
            console.log(e);
          });
      },

      newTarot() {
        this.submitted = false;
        this.tutorial = {};
      }
    }
  };
  </script>

  <style>
  .submit-form {
    max-width: 300px;
    margin: auto;
  }
  </style>
