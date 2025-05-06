<template>
  <v-sheet border rounded>
    <v-data-table :headers="headers" :hide-default-footer="cards.length < 5" :items="cards">
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>
            <v-icon color="medium-emphasis" icon="mdi-book-multiple" size="x-small" start></v-icon>
            Tarot cards
          </v-toolbar-title>
          <v-btn class="me-2" prepend-icon="mdi-plus" rounded="lg" text="Add a card" border @click="add"></v-btn>
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
        <v-checkbox-btn name="major" false-icon="mdi-checkbox-blank-outline" true-icon="mdi-checkbox-marked"
          :model-value="value" readonly></v-checkbox-btn>
      </template>
      <template v-slot:[`item.img`]="{ item }">
        <v-img aspect-ratio="1" :src="getImageSource(item.img)" width="50" height="100" class="bg-white" rounded
          readonly></v-img>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <div class="d-flex ga-2 justify-end">
          <v-icon color="medium-emphasis" icon="mdi-pencil" size="small" @click="edit(item.id)"></v-icon>

          <v-icon color="medium-emphasis" icon="mdi-delete" size="small" @click="remove(item.id)"></v-icon>
        </div>
      </template>
      <template v-slot:no-data>
        <v-btn prepend-icon="mdi-backup-restore" rounded="lg" text="Reset data" variant="text" border
          @click="reset"></v-btn>
      </template>
    </v-data-table>
    <template>
      <AskDialog ref="askDialogRef" title="Add Card" message="Are you sure you want to add a new card"
        :visible="dialogVisible"></AskDialog>
    </template>
    <v-alert v-if="errorMessage.trim()" type="error" dismissible>
      {{ errorMessage }}
    </v-alert>
  </v-sheet>

  <v-dialog v-model="dialog" max-width="500">
    <v-card :subtitle="`${isEditing ? 'Update' : 'Create'} your favorite card`"
      :title="`${isEditing ? 'Edit' : 'Add'} a card`">
      <template v-slot:text>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="record.name"
              label="Card Name"
              :rules="cardValidationRules.name"
              :error-messages="nameErrors"
              @update:model-value="validateName">
            </v-text-field>
          </v-col>
          <v-col cols="8" md="4">
            <v-img
              class="bg-white"
              :src="getImageSource(record.img)"
              v-model="record.img"
              width="150"
              length="150"
              :error-messages="imageErrors"
              @error="handleImageError" >
              <template v-slot:error >
                <div class="text-error">
                  {{  imageErrors }}
                </div>
              </template>
            </v-img>
          </v-col>
          <v-col cols="4" md="2">
            <v-switch direction="vertical" v-model="record.major" label="Major Arcana"></v-switch>
          </v-col>
        </v-row>

        <v-divider></v-divider>
        <v-row>
          <v-col cols="12">
            <v-slide-group v-model="images" class="pa-4" next-icon="mdi-plus" prev-icon="mdi-minus"
              selected-class="bg-primary" show-arrows>
              <v-slide-group-item v-for="(image, index) in images" :key="index"
                v-slot="isSelected, toggle, selectedClass">
                <v-card :class="['ma-4', selectedClass]" color="grey-lighten-1" height="200" width="100"
                  @click="record.img = image.value">
                  <div class="d-flex fill-height align-center justify-center">
                    <v-scale-transition>
                      <v-img :src="getImageSource(image.value)" color="blue" size="48"> </v-img>
                    </v-scale-transition>
                  </div>
                </v-card>
              </v-slide-group-item>
            </v-slide-group>
          </v-col>
        </v-row>
        <v-divider></v-divider>
      </template>

      <!-- Adds a light background to the card actions section for better visual separation -->
      <v-card-actions class="bg-surface-dark">
        <v-btn text="Cancel" variant="plain" @click="dialog = false"></v-btn>
        <v-spacer></v-spacer>
        <v-btn text="Save" @click="save"></v-btn>
      </v-card-actions>
    </v-card>
    <template v-slot:error>
    <v-alert type="error" dense>
      <div v-for="error in nameErrors" :key="error" class="error-message">
        {{ error }}
      </div>
    </v-alert>
  </template>
  </v-dialog>

</template>

<script setup>
import { onMounted, ref, shallowRef } from 'vue'
import TarotDataService from '../services/api/TarotDataService'
import AskDialog from '@/components/askDialog.vue'
import cardValidationRules from '@/types/cardRules'
const nameErrors = ref([])
const imageErrors = ref([])

const DEFAULT_IMAGE = 'src/assets/cards/cover.png'

// Ensure cardValidationRules.name is an array during initialization
if (!Array.isArray(cardValidationRules.name)) {
  console.error('cardValidationRules.name is not an array. Validation may not work as expected.')
  cardValidationRules.name = []
}

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

/**
 * The default structure for a tarot card record.
 *
 * Properties:
 * - `id` (null | number): The unique identifier for the card. Defaults to `null`.
 * - `name` (string): The name of the card. Defaults to an empty string.
 * - `major` (boolean): Indicates whether the card is a major arcana card. Defaults to `false`.
 * - `img` (string): The URL or path to the card's image. Defaults to an empty string.
 */
const DEFAULT_RECORD = {
  id: null,
  name: '',
  major: false,
  img: "",
}

// Reactive variables
const cards = ref([])
const record = ref(DEFAULT_RECORD)
const dialog = shallowRef(false)
const dialogVisible = shallowRef(false)
const isEditing = shallowRef(false)
// const openAskDialog = ref(false)

const errorMessage = ref('')
const askDialogRef = ref(null) // Define the ref for AskDialog
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
  reset()
})


/**
 * Opens the dialog for adding a new record.
 * - Sets `isEditing` to `false` to indicate that the dialog is in "add" mode.
 * - Resets the `record` to a default state using `DEFAULT_RECORD`.
 * - Displays the dialog by setting `dialog` to `true`.
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
 * with the specified ID in the `cards` array, and if found, populates
 * the `record` object with the card's details. If the card is not found,
 * an error message is set. Finally, it opens the dialog for editing.
 *
 * @param {number|string} id - The ID of the card to edit.
 *
 * Reactive Dependencies:
 * - `isEditing` (boolean): Indicates whether the editing mode is active.
 * - `cards` (array): The list of card objects to search within.
 * - `errorMessage` (string): Holds the error message if the card is not found.
 * - `record` (object): The object to populate with the card's details for editing.
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
  const answer = await openAskDialog()
  if (!answer) {
    return
  } else {
    const index = cards.value.findIndex((card) => card.id === id)
    const response = await TarotDataService.delete(id)
    console.log(response.data)
    if (response.status === 200) {
      console.log('Card deleted successfully')
    } else {
      console.error('Failed to delete card')
    }
    if (index !== -1) {
      cards.value.splice(index, 1)
    }
  }
}

/**
 * Asynchronous function to save a card record. This function handles both
 * creating a new card and updating an existing card, depending on the
 * `isEditing` state. It performs validation on the card's name and image
 * before proceeding with the save operation. If validation errors are
 * present, it displays an error message and halts the save process.
 *
 * Workflow:
 * 1. Validates the `name` and `img` fields of the `record`.
 * 2. If validation errors exist, sets an error message and exits.
 * 3. If editing (`isEditing` is true):
 *    - Finds the card by its `id` in the `cards` list.
 *    - Opens a confirmation dialog (`openAskDialog`).
 *    - If confirmed, sends an update request to `TarotDataService.update`.
 *    - Logs success or failure and closes the dialog on success.
 * 4. If creating a new card:
 *    - Opens a confirmation dialog (`openAskDialog`).
 *    - If confirmed, sends a create request to `TarotDataService.create`.
 *    - Logs success or failure and closes the dialog on success.
 * 5. Resets the form state after saving.
 *
 * Error Handling:
 * - Catches any errors during the save process and logs them.
 * - Sets a generic error message if an exception occurs.
 *
 * Dependencies:
 * - `validateName`: Function to validate the card's name.
 * - `validateImage`: Function to validate the card's image.
 * - `openAskDialog`: Function to open a confirmation dialog.
 * - `TarotDataService`: Service for interacting with the backend API.
 * - `reset`: Function to reset the form state.
 *
 * Reactive Variables:
 * - `record`: The card record being edited or created.
 * - `nameErrors`: Array of validation errors for the name field.
 * - `imageErrors`: Array of validation errors for the image field.
 * - `errorMessage`: Error message to display to the user.
 * - `isEditing`: Boolean indicating whether the user is editing an existing card.
 * - `cards`: List of all card records.
 * - `dialog`: Boolean controlling the visibility of the dialog.
 */
async function save() {
  try {
    validateName(record.value.name)
    validateImage(record.value.img)

    if (nameErrors.value.length > 0 || imageErrors.value.length > 0) {
      errorMessage.value = 'Please fix the validation errors before saving.'
      return
    }

    if (isEditing.value) {
      const index = cards.value.findIndex((card) => card.id === record.value.id)
      const answer = await openAskDialog()
      if (answer) {
        const response = await TarotDataService.update(parseInt(cards.value[index].id), record.value)
        console.log('Card updated successfully:', response.data)
        if (response.status === 200) {
          dialog.value = false
        }
        else {
          console.error('Failed to update card')
        }
      }
      } else {
        const answer = await openAskDialog()
        if (answer) {
          const response = await TarotDataService.create(record.value)
          if (response.status === 200) {
            dialog.value = false
            console.log('Card created successfully:', response.data)
          }
          else {
            console.error('Failed to create card')
            dialog.value = false
          }
      }
    }
    reset()
  } catch (error) {
    console.error('Error in save:', error)
    errorMessage.value = 'An error occurred while saving.'
  }
}

/**
 * Resets the card list to its default state and performs the following actions:
 * - Resets the `cards` array to contain a single default record.
 * - Fetches updated items by calling `fetchItems()`.
 * - Closes the dialog by setting `dialog` to `false`.
 * - Disables editing mode by setting `isEditing` to `false`.
 */
function reset() {
  cards.value = [JSON.parse(JSON.stringify(DEFAULT_RECORD))]
  fetchItems()
  dialog.value = false
  isEditing.value = false
}

/**
 * Fetches tarot card items from the TarotDataService and updates the `cards` reactive variable.
 * Each card object is modified to exclude the `actions` property.
 * If an error occurs during the fetch operation, logs the error to the console
 * and updates the `errorMessage` reactive variable with a user-friendly message.
 *
 * @async
 * @function fetchItems
 * @returns {Promise<void>} Resolves when the fetch operation is complete.
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
 * Opens a confirmation dialog with a specified title and message.
 *
 * This function sets the `dialogVisible` state to `true` and then calls the `open` method
 * on the `askDialogRef` reference to display a dialog box. The dialog box includes a title
 * and a message prompting the user to confirm their action.
 *
 * @returns {Promise} A promise that resolves when the dialog interaction is completed.
 */
async function openAskDialog() {
  dialogVisible.value = true
  return await askDialogRef.value.open({
    title: 'Confirm Action',
    message: 'Are you sure you want to proceed?',
  })
}

/**
 * Validates the provided name value against a set of validation rules.
 *
 * The function checks if `cardValidationRules.name` is an array of validation
 * rules. If it is, each rule is applied to the provided `value`. Any validation
 * errors are collected and stored in the `nameErrors` reactive variable.
 * If `cardValidationRules.name` is not an array, a default error message is
 * added to `nameErrors`.
 *
 * @param {string} value - The name value to be validated.
 *
 * Reactive Dependencies:
 * - `cardValidationRules.name`: An array of validation rules or undefined.
 * - `nameErrors`: A reactive variable to store validation error messages.
 *
 * Validation Rules:
 * Each rule in `cardValidationRules.name` should be a function that takes a
 * string value as input and returns:
 * - `true` if the value passes the rule.
 * - A string error message if the value fails the rule.
 */
function validateName(value) {
  if (Array.isArray(cardValidationRules.name)) {
    const errors = []
    for (const rule of cardValidationRules.name) {
      const result = rule(value)
      if (result !== true) {
        errors.push(result)
      }
    }
    nameErrors.value = errors
  } else {
    nameErrors.value = ['Name Validation rules are not properly defined.']
  }
}

/**
 * Validates the provided image value against a set of predefined validation rules.
 *
 * The function checks if `cardValidationRules.img` is an array of validation rules.
 * If it is, each rule is applied to the provided `value`. Any validation errors
 * are collected and stored in `imageErrors.value`. If all rules pass, no errors
 * are added. If `cardValidationRules.img` is not an array, a default error message
 * is added to indicate improper configuration of validation rules.
 *
 * @param {any} value - The image value to be validated.
 *
 * Side Effects:
 * - Updates the `imageErrors.value` reactive property with an array of error messages
 *   if validation fails, or an empty array if validation succeeds.
 */
function validateImage(value) {
  if (Array.isArray(cardValidationRules.img)) {
    const errors = []
    for (const rule of cardValidationRules.img) {
      const result = rule(value)
      if (result !== true) {
        errors.push(result)
      }
    }
    imageErrors.value = errors
  } else {
    imageErrors.value = ['Image Validation rules are not properly defined.']
  }
}

/**
 * Handles the error event for the image component.
 * - Sets the `imageErrors` reactive variable to indicate that the image failed to load.
 *
 * @returns {void}
 */
function handleImageError() {
  imageErrors.value = ['Failed to load image']
}

/* Fetches a list of tarot images and returns them as an array of objects.
 *
 * This function creates an object mapping of tarot image filenames to their respective paths.
 * It then converts this object into an array of objects, each containing a `key` and `value`
 * property representing the filename and its path, respectively.
 *
 * @returns {Array} An array of objects representing tarot images and their paths.
 */
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
