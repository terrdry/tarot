/**
 * Test suite for the VuetifyButtonTest component.
 *
 * @module VuetifyButtonTest.spec
 *
 * @requires vue-test-utils/mount - Utility for mounting Vue components in tests.
 * @requires ./VuetifyButtonTest.vue - The VuetifyButtonTest component being tested.
 * @requires vuetify/createVuetify - Function to create a Vuetify instance.
 * @requires vitest/describe - Function to group related tests.
 * @requires vitest/it - Function to define individual test cases.
 * @requires vitest/expect - Assertion library for testing.
 * @requires vuetify/styles - Vuetify styles for component rendering.
 * @requires vuetify/components - Vuetify components for use in the application.
 * @requires vuetify/directives - Vuetify directives for use in the application.
 */
import { mount } from '@vue/test-utils'
import VuetifyButtonTest from './VuetifyButtonTest.vue'
import { describe, it, expect } from 'vitest'

describe('VuetifyButtonTest.vue', () => {
  it('renders a Vuetify button with correct text', () => {
    /**
     * Mounts the VuetifyButtonTest component for testing purposes.
     *
     * @constant {Wrapper} wrapper - The wrapper instance for the VuetifyButtonTest component.
     * @property {Object} global - Configuration for the global mounting options.
     * @property {Array} global.plugins - An array of plugins to be installed, including Vuetify.
     */
    const wrapper = mount(VuetifyButtonTest)
    expect(wrapper.text()).toContain('Click me')
  })
})
