import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils';
import CardList from '../components/CardList.vue';
import axios from 'axios';
import { jest } from 'globals';
import { flushPromises } from 'flush-promises';

jest.mock('axios');

describe('CardList.vue', () => {
  it('fetches cards from API and displays them', async () => {
    const cards = [{ id: 1, title: 'Test Card' }];
    axios.get.mockResolvedValue({ data: cards });

    const wrapper = mount(CardList);
    await flushPromises();

    expect(wrapper.text()).toContain('Test Card');
  });
});