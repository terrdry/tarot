import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils';
import CardList from '../CardList.vue';
// import axios from 'axios';
// import { jest } from 'globals';
// import { flushPromises } from 'flush-promises';

// jest.mock('axios');


describe(  'Main View', () => {
  it('See if the title is correct', () => {
    // const wrapper = mount(CardList, { props: { item: [ ]  } } )
    const wrapper = mount(CardList, { } )
    // expect(wrapper.text()).toContain('Items' )
    expect(wrapper.text()).toContain('Items' )
  })
})