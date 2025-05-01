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
        <v-img
          :src="getImageSource(item.img)"
          width="100"
          max-width="50"
          height="200"
          max-height="100"
          class="bg-white"
          rounded
          readonly
        ></v-img>
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
    <!-- <template>
      <AskDialog
        ref="askDialogRef"
        title="Add Card"
        message="Are you sure you want to add a new card"
        :visible="dialogVisible"
      ></AskDialog>
    </template> -->
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
          <v-col cols="8" md="4">
            <v-img
              class="bg-white"
              :src="getImageSource(record.img)"
              v-model="record.img"
              width="150"
              length="150"
            >
            </v-img>
          </v-col>
          <v-col cols="4" md="2">
            <v-switch direction="vertical" v-model="record.major" label="Major Arcana"></v-switch>
          </v-col>
        </v-row>

        <v-divider></v-divider>
        <v-row>
          <v-col cols="12">
            <v-slide-group
              v-model="images"
              class="pa-4"
              next-icon="mdi-plus"
              prev-icon="mdi-minus"
              selected-class="bg-primary"
              show-arrows
            >
              <v-slide-group-item
                v-for="(image, index) in images"
                :key="index"
                v-slot="isSelected, toggle, selectedClass"
                >

                <v-card
                  :class="['ma-4', selectedClass]"
                  color="grey-lighten-1"
                  height="200"
                  width="100"
                  @click="record.img = image.value"
                >
                  <div class="d-flex fill-height align-center justify-center">
                    <v-scale-transition>
                      <v-img
                        :src="getImageSource(image.value)"
                        color="blue"
                        size="48"
                      >
                      </v-img>
                    </v-scale-transition>
                  </div>
                </v-card>
              </v-slide-group-item>
            </v-slide-group>
          </v-col>
        </v-row>
      </template>

      <!-- Adds a light background to the card actions section for better visual separation -->
      <v-card-actions class="bg-surface-dark">
        <v-btn text="Cancel" variant="plain" @click="dialog = false"></v-btn>
        <v-spacer></v-spacer>
        <v-btn text="Save" @click="save"></v-btn>
        <!-- <v-btn text="Save" @click="save"></v-btn> temporary for testing the click-->
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { onMounted, ref, shallowRef } from 'vue'
import TarotDataService from '../services/api/TarotDataService'
// import AskDialog from '@/components/askDialog.vue'


const DEFAULT_IMAGE = 'src/assets/cards/cover.png'

/**
 * Returns the appropriate image source URL.
 *
 * @param {string} imgUrl - The URL of the image to be used.
 * @returns {string} - The provided image URL if it is a valid string,
 *                     otherwise returns the default image URL (DEFAULT_IMAGE).
 */
function getImageSource(imgUrl) {
  if (typeof imgUrl !== 'string') {
    return DEFAULT_IMAGE
  }
  return imgUrl || DEFAULT_IMAGE
}

// Define the default record structure
const DEFAULT_RECORD = {
  id: null,
  name: '',
  major: false,
  img: '',
}

// Reactive variables
const cards = ref([])
const record = ref(DEFAULT_RECORD)
const dialog = shallowRef(false)
const isEditing = shallowRef(false)
const errorMessage = ref('')

const images = shallowRef(null)

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
  images.value = fetchImages()
  console.log(images.value)
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
 *
 * This function sets the editing state to true, searches for the card
 * with the specified ID in the `cards` list, and populates the `record`
 * object with the card's details if found. If the card is not found,
 * an error message is set. Finally, it opens the dialog for editing.
 *
 * @param {number|string} id - The ID of the card to edit.
 *
 * Reactive Dependencies:
 * - `isEditing` (boolean): Indicates whether the editing mode is active.
 * - `cards` (array): The list of card objects to search through.
 * - `errorMessage` (string): Holds the error message if the card is not found.
 * - `record` (object): The reactive object to store the card's details for editing.
 * - `dialog` (boolean): Controls the visibility of the editing dialog.
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
async function remove(id) {
  const answer = true
  //const answer = await openAskDialog()
  if (!answer) {
    return
  } else {
    const index = cards.value.findIndex((card) => card.id === id)
    if (index !== -1) {
      cards.value.splice(index, 1)
    }
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
      const answer = true
      // const answer = await openAskDialog()
      if (answer) {
        cards.value[index] = { ...record.value }
      }
    } else {
      record.value.id = cards.value.length + 1
      const answer = true
      // const answer = await openAskDialog()
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

const fetchImages = () => {
  const tarotImages = {
    'wands-2.png': 'src/assets//cards/wands-2.png',
    'wands-3.png': 'src/assets//cards/wands-3.png',
    'wands-4.png': 'src/assets//cards/wands-4.png',
    'wands-5.png': 'src/assets//cards/wands-5.png',
    'wands-6.png': 'src/assets//cards/wands-6.png',
    'wands-7.png': 'src/assets//cards/wands-7.png',
    'wands-8.png': 'src/assets//cards/wands-8.png',
    'wands-9.png': 'src/assets//cards/wands-9.png',
    'wands-10.png': 'src/assets//cards/wands-10.png',
    'wands-ace.png': 'src/assets//cards/wands-ace.png',
    'wands-knight.png': 'src/assets//cards/wands-knight.png',
    'wands-queen.png': 'src/assets//cards/wands-queen.png',
    'wands-king.png': 'src/assets//cards/wands-king.png',
    'pentacles-2.png': 'src/assets//cards/pentacles-2.png',
    'pentacles-3.png': 'src/assets//cards/pentacles-3.png',
    'pentacles-4.png': 'src/assets//cards/pentacles-4.png',
    'pentacles-5.png': 'src/assets//cards/pentacles-5.png',
    'pentacles-6.png': 'src/assets//cards/pentacles-6.png',
    'pentacles-7.png': 'src/assets//cards/pentacles-7.png',
    'pentacles-8.png': 'src/assets//cards/pentacles-8.png',
    'pentacles-9.png': 'src/assets//cards/pentacles-9.png',
    'pentacles-10.png': 'src/assets//cards/pentacles-10.png',
    'pentacles-ace.png': 'src/assets//cards/pentacles-ace.png',
    'pentacles-knight.png': 'src/assets//cards/pentacles-knight.png',
    'pentacles-queen.png': 'src/assets//cards/pentacles-queen.png',
    'pentacles-king.png': 'src/assets//cards/pentacles-king.png',
    'swords-2.png': 'src/assets//cards/swords-2.png',
    'swords-3.png': 'src/assets//cards/swords-3.png',
    'swords-4.png': 'src/assets//cards/swords-4.png',
    'swords-5.png': 'src/assets//cards/swords-5.png',
    'swords-6.png': 'src/assets//cards/swords-6.png',
    'swords-7.png': 'src/assets//cards/swords-7.png',
    'swords-8.png': 'src/assets//cards/swords-8.png',
    'swords-9.png': 'src/assets//cards/swords-9.png',
    'swords-10.png': 'src/assets//cards/swords-10.png',
    'swords-ace.png': 'src/assets//cards/swords-ace.png',
    'swords-knight.png': 'src/assets//cards/swords-knight.png',
    'swords-queen.png': 'src/assets//cards/swords-queen.png',
    'swords-king.png': 'src/assets//cards/swords-king.png',
    'cups-2.png': 'src/assets//cards/cups-2.png',
    'cups-3.png': 'src/assets//cards/cups-3.png',
    'cups-4.png': 'src/assets//cards/cups-4.png',
    'cups-5.png': 'src/assets//cards/cups-5.png',
    'cups-6.png': 'src/assets//cards/cups-6.png',
    'cups-7.png': 'src/assets//cards/cups-7.png',
    'cups-8.png': 'src/assets//cards/cups-8.png',
    'cups-9.png': 'src/assets//cards/cups-9.png',
    'cups-10.png': 'src/assets//cards/cups-10.png',
    'cups-ace.png': 'src/assets//cards/cups-ace.png',
    'cups-knight.png': 'src/assets//cards/cups-knight.png',
    'cups-queen.png': 'src/assets//cards/cups-queen.png',
    'cups-king.png': 'src/assets//cards/cups-king.png',
    'fool.png': 'src/assets//cards/fool.png',
    'chariot.png': 'src/assets//cards/chariot.png',
    'death.png': 'src/assets//cards/death.png',
    'devil.png': 'src/assets//cards/devil.png',
    'emperor.png': 'src/assets//cards/emperor.png',
    'empress.png': 'src/assets//cards/empress.png',
    'hangedman.png': 'src/assets//cards/hangedman.png',
    'hermit.png': 'src/assets//cards/hermit.png',
    'hierophant.png': 'src/assets//cards/hierophant.png',
    'highpriestess.png': 'src/assets//cards/highpriestess.png',
    'judgement.png': 'src/assets//cards/judgement.png',
    'justice.png': 'src/assets//cards/justice.png',
    'lovers.png': 'src/assets//cards/lovers.png',
    'magician.png': 'src/assets//cards/magician.png',
    'moon.png': 'src/assets//cards/moon.png',
    'temperance.png': 'src/assets//cards/temperance.png',
    'star.png': 'src/assets//cards/star.png',
    'strength.png': 'src/assets//cards/strength.png',
    'sun.png': 'src/assets//cards/sun.png',
    'tower.png': 'src/assets//cards/tower.png',
    'wheeloffortune.png': 'src/assets//cards/wheeloffortune.png',
    'world.png': 'src/assets/cards/world.png',
  }
  const result = Object.entries(tarotImages).map(([key, value]) => ({
    key,
    value,
  }))
  return result
}
</script>
