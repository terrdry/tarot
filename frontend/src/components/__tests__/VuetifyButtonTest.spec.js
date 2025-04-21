import { mount } from '@vue/test-utils'
import VuetifyButtonTest from './VuetifyButtonTest.vue'
import { createVuetify } from 'vuetify'
import { describe, it, expect } from 'vitest'

import 'vuetify/styles'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

describe('VuetifyButtonTest.vue', () => {
  it('renders a Vuetify button with correct text', () => {
    const wrapper = mount(VuetifyButtonTest, {
      global: {
        plugins: [vuetify],
      },
    })
    expect(wrapper.text()).toContain('Click me')
  })
})
