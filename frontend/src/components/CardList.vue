<template>
  <v-sheet border rounded>
    <v-data-table :headers="headers" :hide-default-footer="cards.length < 5" :items="cards">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>
            <v-icon color="medium-emphasis" icon="mdi-book-multiple" size="x-small" start></v-icon>

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

      <template v-slot:[`item.name`]="{ value }">
        <v-chip :text="value" border="thin opacity-25" prepend-icon="mdi-book" label>
          <template v-slot:prepend>
            <v-icon color="medium-emphasis"></v-icon>
          </template>
        </v-chip>
      </template>

      <template v-slot:[`item.major`]="{ value }">
        <v-checkbox-btn
          name="major"
          false-icon="mdi-checkbox-blank-outline"
          true-icon="mdi-checkbox-marked"
          :model-value="value"
          readonly
        ></v-checkbox-btn>
      </template>

      <template v-slot:[`item.img`]="{ item }">
        <v-img :src="getImageSource(item.img)" :aspect-ratio="1" class="bg-white" readonly></v-img>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
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
    <template>
      <AskDialog
        ref="askDialogRef"
        title="Add Card"
        message="Are you sure you want to add a new card"
        :visible="dialogVisible"
      ></AskDialog>
    </template>
    <v-alert v-if="errorMessage.trim()" type="error" dismissible>
      {{ errorMessage }}
    </v-alert>
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
              class="bg-white"
              :src="getImageSource(record.img)"
              v-model="record.img"
            ></v-img>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-card-text>
          <v-text-field
            v-model="record.img"
            label="Image URL"
            placeholder="https://example.com/image.jpg"
          ></v-text-field>
        </v-card-text>
      </template>

      <!-- Adds a light background to the card actions section for better visual separation -->
      <v-card-actions class="bg-surface-dark">
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
import AskDialog from '@/components/askDialog.vue'

const DEFAULT_IMAGE = 'https://cdn.vuetifyjs.com/images/parallax/material.jpg'

function getImageSource(imgUrl) {
  if (typeof imgUrl !== 'string') {
    return DEFAULT_IMAGE
  }
  return imgUrl || DEFAULT_IMAGE
}

const DEFAULT_RECORD = {
  id: null,
  name: '',
  major: false,
  img: '',
}
// Reactive variable to store the list of tarot cards.
// This array is dynamically updated as cards are added, edited, or removed.
const cards = ref([])
const record = ref(DEFAULT_RECORD)
const dialog = shallowRef(false)
const isEditing = shallowRef(false)
const dialogVisible = ref(false)
const errorMessage = ref('')
const askDialogRef = ref(null) // Define the ref for AskDialog
const askDialogHandlers = ref(null) // Define the ref for dialog handlers

const headers = [
  { title: 'Name', key: 'name', align: 'start' },
  { title: 'Major Arcana', key: 'major' },
  { title: 'Image', key: 'img' },
  { title: 'Actions', key: 'actions', align: 'end', sortable: false },
]

/**
 * Lifecycle hook that is called when the component is mounted.
 * This hook triggers the `reset` function to initialize or reset
 * the component's state when it is first rendered.
 */
onMounted(() => {
  reset()
})

/**
 * Opens a dialog for adding a new record.
 *
 * This function performs the following actions:
 * - Sets the `isEditing` state to `false` to indicate that the dialog is not in editing mode.
 * - Resets the `record` to the default record value (`DEFAULT_RECORD`).
 * - Sets the `dialog` state to `true` to display the dialog.
 *
 * @returns {Promise<void>} This function does not return a value.
 */
function add() {
  isEditing.value = false
  record.value = { ...DEFAULT_RECORD }

  dialog.value = true
}

/**
 * Edits a card by its ID.
 * - Sets the `isEditing` flag to true.
 * - Finds the card with the given ID and populates the `record` object with its details.
 * - Opens the dialog for editing.
 *
 * @param {number} id - The ID of the card to edit.
 */
function edit(id) {
  isEditing.value = true
  const found = cards.value.find((card) => card.id === id)

  if (!found) {
    errorMessage.value = 'Card not found.'
    return
  }

  record.value = {
    id: found.id,
    name: found.name,
    major: found.major,
    img: found.img,
  }
  dialog.value = true
}

/**
 * Removes a card by its ID.
 * - Finds the index of the card with the given ID and removes it from the `cards` array.
 * - If no card with the given ID is found, logs a warning and does nothing.
 *
 * @param {number} id - The ID of the card to remove.
 */
function remove(id) {
  const answer = openAskDialog()
  if (!answer) {
    return
  }
  else {
    const index = cards.value.findIndex((card) => card.id === id)
    cards.value.splice(index, 1)
  }

}

/**
 * Saves the current record to the cards list.
 * - If `isEditing` is true, it updates the existing card.
 * - If `isEditing` is false, it adds a new card.
 * - Closes the dialog after saving.
 */
async function save() {
  try {
    if (isEditing.value) {
      const index = cards.value.findIndex((card) => card.id === record.value.id)
      const answer = await openAskDialog()
      if (answer) {
        cards.value[index] = { ...record.value }
      }
    } else {
      record.value.id = cards.value.length + 1
      const answer = await openAskDialog()
      if (answer) {
        cards.value.push({ ...record.value })
      }
    }
    dialog.value = false
  } catch (error) {
    console.error('Error in save:', error)
    errorMessage.value = 'An error occurred while saving.'
  }
}
/**
 * Resets the card list to its default state.
 * - Resets the `cards` array to contain only the default record.
 * - Fetches items to repopulate the list.
 * - Closes the dialog and resets the `isEditing` flag.
 */
function reset() {
  cards.value = [JSON.parse(JSON.stringify(DEFAULT_RECORD))]
  fetchItems()
  dialog.value = false
  isEditing.value = false
}

/**
 * Fetches a list of tarot cards from the TarotDataService and updates the `cards` reactive variable.
 * Each card object is mapped to exclude the `actions` property.
 *
 *
 * @async
 * @function fetchItems
 * @throws Will log an error to the console if the request to fetch items fails.
 */
const fetchItems = async () => {
  try {
    const response = await TarotDataService.getAll()
    cards.value = response.data.map((card) => ({
      ...card,
      actions: undefined,
    }))
  } catch (error) {
    console.error('Error fetching items:', error)
    errorMessage.value = 'Failed to fetch tarot cards. Please try again later.'
  }
}

/**
 * Opens a confirmation dialog and returns a promise that resolves based on user action.
 */
async function openAskDialog() {
  // Check if dialog ref exists before proceeding
  // if (!dialogVisible.value) {
  //   console.warn('AskDialog reference not found');
  //   return false;
  // }
  // Show the dialog and return the promise from open()
  dialogVisible.value = true
  return askDialogRef.value.open({
    title: 'Confirm Action',
    message: 'Are you sure you want to proceed?',
  })
}
</script>
<style scoped></style>
