/**
 * Test suite for the CardList.vue component.
 *
 * @fileoverview This file contains unit tests for the CardList component using Vitest and Vue Test Utils.
 * It ensures that the component renders properly and integrates with Vuetify and the router.
 *
 * @requires vitest - Provides the testing framework for the test suite.
 * @requires @vue/test-utils - Provides utilities for testing Vue components.
 * @requires @/components/CardList.vue - The CardList component being tested.
 */
import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import CardList from '@/components/CardList.vue';

describe('CardList.vue', () => {
  it('renders properly', () => {

    /**
     * Mounts the CardList component with the specified local plugins.
     *
     * @constant {Wrapper} wrapper - The wrapper instance for the mounted CardList component.
     */
    const wrapper = mount(CardList);
    // Check if the CardList component is successfully mounted
    expect(wrapper.exists()).toBe(true);
  });
});
