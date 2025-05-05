<template>
    <v-dialog v-model="dialogVisible" transition="dialog-top-transition" width="auto">
      <v-card>
        <v-card-title>{{ dialogTitle }}</v-card-title>
        <v-card-text>{{ dialogMessage }}</v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn text @click="handleCancel">Cancel</v-btn>
          <v-btn color="primary" text @click="handleConfirm">Confirm</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script setup>
import { ref } from 'vue'
const dialogVisible = ref(false)
const resolveFn = ref(null)
const dialogTitle = ref('Are you sure?')
const dialogMessage = ref('Please confirm your action.')

/**
 * Opens a dialog with the specified options.
 *
 * @param {Object} [options={}] - Configuration options for the dialog.
 * @param {string} [options.title='Are you sure?'] - The title of the dialog.
 * @param {string} [options.message='Please confirm your action.'] - The message displayed in the dialog.
 * @returns {Promise} A promise that resolves when the dialog action is confirmed.
 */
function open(options = {}) {
  dialogTitle.value = options.title || 'Are you sure?'
  dialogMessage.value = options.message || 'Please confirm your action.'
  dialogVisible.value = true

  return new Promise((resolve) => {
    resolveFn.value = resolve
  })
}

/**
 * Handles the confirmation action for the dialog.
 *
 * This function is triggered when the user confirms the dialog. It performs the following actions:
 * 1. Hides the dialog by setting `dialogVisible` to `false`.
 * 2. Resolves the promise associated with the dialog using `resolveFn` if it is defined.
 * 3. Logs an error to the console if `resolveFn` is not defined, including details about the dialog title and message.
 * 4. Resets `resolveFn` to `null` after handling the confirmation.
 *
 * Note: Ensure that `resolveFn` is properly initialized before calling this function to avoid errors.
 */
function handleConfirm() {
  dialogVisible.value = false
  if (resolveFn.value) {
    resolveFn.value(true)
  } else {
    console.error(`resolveFn is not defined. The promise could not be resolved. Dialog Title: "${dialogTitle.value}", Dialog Message: "${dialogMessage.value}".`)
  }
  resolveFn.value = null
}

/**
 * Handles the cancel action for the dialog.
 * This function is triggered when the user cancels the dialog,
 * allowing for any necessary cleanup or state updates.
 */
function handleCancel() {
  dialogVisible.value = false
  if (resolveFn.value) {
    resolveFn.value(false)
  } else {
    console.warn('resolveFn is not defined. The promise could not be resolved.')
  }
  resolveFn.value = null
}

// Expose the `open` method to the parent component, allowing it to trigger this dialog.
defineExpose({ open })
</script>
