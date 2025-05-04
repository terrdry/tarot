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

function open(options = {}) {
  dialogTitle.value = options.title || 'Are you sure?'
  dialogMessage.value = options.message || 'Please confirm your action.'
  dialogVisible.value = true

  return new Promise((resolve) => {
    resolveFn.value = resolve
  })
}

function handleConfirm() {
  dialogVisible.value = false
  if (resolveFn.value) {
    resolveFn.value(true)
  } else {
    console.error(`resolveFn is not defined. The promise could not be resolved. Dialog Title: "${dialogTitle.value}", Dialog Message: "${dialogMessage.value}".`)
  }
  resolveFn.value = null
}

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
