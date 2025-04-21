<!-- eslint-disable vue/valid-v-slot -->
<!-- TODO will add validation of all fields -->

<template>
  <v-sheet border rounded>
    <v-data-table
      :headers="headers"
      :hide-default-footer="cards.length < 5"
      :items="cards"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>
            <v-icon
              color="medium-emphasis"
              icon="mdi-book-multiple"
              size="x-small"
              start
            ></v-icon>

            Tarot cards
          </v-toolbar-title>

          <v-btn
            class="me-2"
            prepend-icon="mdi-plus"
            rounded="lg"
            text="Add a card"
            border
            @click="add"
          ></v-btn>
        </v-toolbar>
      </template>

      <template v-slot:item.name="{ value }">
        <v-chip
          :text="value"
          border="thin opacity-25"
          prepend-icon="mdi-book"
          label
        >
          <template v-slot:prepend>
            <v-icon color="medium-emphasis"></v-icon>
          </template>
        </v-chip>
      </template>

      <template v-slot:item.major="{ value }">
        <v-checkbox-btn
          false-icon="mdi-checkbox-blank-outline"
          true-icon="mdi-checkbox-marked"
          :model-value="value"
          readonly
        ></v-checkbox-btn>
      </template>

      <template v-slot:item.img="{ value }">
        <v-img
          :aspect-ration='1'
          class="bg-white"
          src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
          true-icon="mdi-checkbox-marked"
          :model-value="value"
          readonly
        ></v-img>
      </template>

      <template v-slot:item.actions="{ item }">
        <div class="d-flex ga-2 justify-end">
          <v-icon
            color="medium-emphasis"
            icon="mdi-pencil"
            size="small"
            @click="edit(item.id)"
          ></v-icon>

          <v-icon
            color="medium-emphasis"
            icon="mdi-delete"
            size="small"
            @click="remove(item.id)"
          ></v-icon>
        </div>
      </template>

      <template v-slot:no-data>
        <v-btn
          prepend-icon="mdi-backup-restore"
          rounded="lg"
          text="Reset data"
          variant="text"
          border
          @click="reset"
        ></v-btn>
      </template>
    </v-data-table>
  </v-sheet>

  <v-dialog v-model="dialog" max-width="500">
    <v-card
      :subtitle="`${isEditing ? 'Update' : 'Create'} your favorite card`"
      :title="`${isEditing ? 'Edit' : 'Add'} a card`"
    >
      <template v-slot:text>
        <v-row>
          <v-col cols="12">
            <v-text-field v-model="record.name" label="Card Name"></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-checkbox-btn v-model="record.major" label="major"></v-checkbox-btn>
          </v-col>

          <v-col cols="12" md="6">
            <v-img
              :aspect-ration='1'
              class="bg-white"
              src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
              v-model="record.img"
            ></v-img>
          </v-col>


        </v-row>
      </template>

      <v-divider></v-divider>

      <v-card-actions class="bg-surface-light">
        <v-btn text="Cancel" variant="plain" @click="dialog = false"></v-btn>

        <v-spacer></v-spacer>

        <v-btn text="Save" @click="save"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
  import { onMounted, ref, shallowRef } from 'vue'
  import TarotDataService from '../services/api/TarotDataService'

  const DEFAULT_RECORD = {
    name: '',
    major: false,
    img: '',
  }

  const cards = ref([])
  const record = ref(DEFAULT_RECORD)
  const dialog = shallowRef(false)
  const isEditing = shallowRef(false)

  const headers = [
    { title: 'Name', key: 'name', align: 'start' },
    { title: 'Major Arcana', key: 'major' },
    { title: 'Image', key: 'img' },
    { title: 'Actions', key: 'actions', align: 'end', sortable: false },
  ]

  onMounted(() => {
    reset()
  })

  function add() {
    isEditing.value = false
    record.value = DEFAULT_RECORD
    dialog.value = true
  }

  function edit(id) {
    isEditing.value = true

    const found = cards.value.find(card => card.id === id)

    record.value = {
      id: found.id,
      name: found.name,
      major: found.major,
      img: found.img,
      actions: undefined
    }

    dialog.value = true
  }

  function remove(id) {
    const index = cards.value.findIndex(card => card.id === id)
    cards.value.splice(index, 1)
  }

  function save() {
    if (isEditing.value) {
      const index = cards.value.findIndex(card => card.id === record.value.id)
      cards.value[index] = record.value
    } else {
      record.value.id = cards.value.length + 1
      // ## TODO need to do an add

    }

    dialog.value = false
  }

  function reset() {
    cards.value = [ DEFAULT_RECORD]
    fetchItems()
    dialog.value = false
    isEditing.value = false
}
const fetchItems = async () => {
  try {
    const response = await TarotDataService.getAll()
    cards.value = response.data.map(card => ({
      ...card,
      actions: undefined,
    })
  )
    console.log(cards.value)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}
</script>
<style scoped>
</style>
