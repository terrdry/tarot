/**
 * Test suite for the HelloWorld component.
 *
 * @module HelloWorld.spec
 * @requires vitest - Testing framework for running the test suite.
 * @requires @vue/test-utils - Utility library for testing Vue components.
 * @requires @/components/HelloWorld.vue - The HelloWorld Vue component being tested.
 */
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld.vue'

/**
 * Test case to verify that the HelloWorld component renders properly.
 *
 * @function
 * @name rendersProperly
 * @description Mounts the HelloWorld component with a message prop and checks if the rendered text contains the message.
 * @param {string} message - The message to be passed as a prop to the HelloWorld component.
 * @returns {void}
 */
describe('HelloWorld', () => {
  it('renders properly', () => {
    var message = 'echo one two'
    /**
     * Mounts the HelloWorld component with the specified props.
     *
     * @constant
     * @type {Wrapper<Vue>}
     * @param {Object} HelloWorld - The Vue component to be mounted.
     * @param {Object} options - The options for mounting the component.
     * @param {Object} options.props - The props to pass to the component.
     * @param {string} options.props.msg - The message prop to be passed to the HelloWorld component.
     */
    const wrapper = mount(HelloWorld, { props: { msg: message } })
    expect(wrapper.text()).toContain(message)
  })
})
