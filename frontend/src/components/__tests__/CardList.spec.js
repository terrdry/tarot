import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils';
import CardList from '@/components/CardList.vue';
import router from '@/router'


describe('Main View', () => {
  it('See if the title is correct', () => {
    // const wrapper = mount(CardList, { props: { item: [ ]  } } )
    const wrapper = mount(CardList, {
      global: {
        plugins: [router],
      }
    });
    // expect(wrapper.text()).toContain('Items' )
    expect(wrapper.text()).toContain('Items')
  })
})