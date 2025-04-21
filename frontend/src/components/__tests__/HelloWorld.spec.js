import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import HelloWorld from '../HelloWorld.vue'

describe.skip('HelloWorld', () => {
  it('renders properly', () => {
    var message = 'echo one two'
    const wrapper = mount(HelloWorld, { props: { msg: message } })
    expect(wrapper.text()).toContain(message)
  })
})
