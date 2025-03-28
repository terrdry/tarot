import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils';
import CardList from '../CardList.vue';
// import axios from 'axios';
// import { jest } from 'globals';
// import { flushPromises } from 'flush-promises';

// jest.mock('axios');


describe(  "THis is a test to do something useful", () => {
  it('renders properly', () => {
    const wrapper = mount(CardList, {props: {msg: "Hello Vitest"}})
    expect(wrapper.text()).toContain('Oppostiorn' )
  })
})