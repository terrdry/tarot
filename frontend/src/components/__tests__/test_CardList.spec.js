import { describe, it, expect, beforeEach, vi } from 'vitest'
import { ref } from 'vue'
import CardList from '@/components/CardList.vue'

describe('CardList Component Tests', () => {
    const DEFAULT_RECORD = {
        id: null,
        name: '',
        major: false,
        img: '',
    }
    let testComponent

    beforeEach(() => {
        vi.clearAllMocks()
        testComponent = ref({
            dialog: false,
            isEditing: false,
            record: { ...DEFAULT_RECORD },
            cards: [],
            add: vi.fn(() => {
                testComponent.value.record = { ...DEFAULT_RECORD }
                testComponent.value.dialog = true
                testComponent.value.isEditing = false

            }),
            edit: vi.fn((id) => {
                const card = testComponent.value.cards.find(card => card.id === id)
                if (card) {
                    testComponent.value.record = { ...card }
                    testComponent.value.dialog = true
                    testComponent.value.isEditing = true
                }
            }),
            remove: vi.fn(),
            reset: vi.fn(() => {
                testComponent.value.cards = [{ id: null, name: '', major: false, img: '' }];
            }),
            save: vi.fn().mockImplementation(async () => {
                const record = testComponent.value.record
                if (record.id === null) {
                    record.id = testComponent.value.cards.length + 1
                    testComponent.value.cards.push({ ...record })
                } else {
                    const index = testComponent.value.cards.findIndex(card => card.id === record.id)
                    if (index !== -1) {
                        testComponent.value.cards[index] = { ...record }
                    }
                }
                testComponent.value.dialog = false
                testComponent.value.isEditing = false
                },
            )
        })

    })
        it('should initialize with default values', () => {
            expect(testComponent.value.dialog).toBe(false)
            expect(testComponent.value.isEditing).toBe(false)
            expect(testComponent.value.cards).toEqual([])
            expect(testComponent.value.record).toEqual(DEFAULT_RECORD)
        })

        it('should test adding a card', () => {
            testComponent.value.add()
            expect(testComponent.value.add).toHaveBeenCalled()
            expect(testComponent.value.dialog).toBe(true)
            expect(testComponent.value.isEditing).toBe(false)
        })

        it('should test editing a card', () => {
            testComponent.value.cards = [
                { id: 1, name: 'The Fool', major: true, img: 'https://example.com/fool.jpg' },
            ]
            testComponent.value.edit(1)
            expect(testComponent.value.dialog).toBe(true)
            expect(testComponent.value.isEditing).toBe(true)
            expect(testComponent.value.record.name).toBe('The Fool')
        })

        it.skip('should test removing a card', async () => {
            testComponent.value.cards = [
                { id: 1, name: 'The Fool', major: true, img: 'https://example.com/fool.jpg' },
            ]
            await testComponent.value.remove(1)
            expect(testComponent.value.cards.length).toBe(0)
        })

        it.skip('should test saving a card', async () => {
            testComponent.value.record = { id: null, name: 'The Magician', major: true, img: 'https://example.com/magician.jpg' }
            expect(testComponent.value.cards.length).toBe(1)
            expect(testComponent.value.cards[0].name).toBe('The Magician')
            expect(testComponent.value.save).toHaveBeenCalledWith(testComponent.value.record)
            expect(testComponent.value.cards.length).toBe(1)
            expect(testComponent.value.cards[0].name).toBe('The Magician')

            testComponent.value.isEditing = true
            expect(testComponent.value.cards[0].name).toBe('The High Priestess')
            expect(testComponent.value.save).toHaveBeenCalledWith(testComponent.value.record)
            await testComponent.value.save()
            expect(testComponent.value.cards[0].name).toBe('The High Priestess')
        })

        it('should test resetting cards', () => {
            testComponent.value.cards = []
            testComponent.value.reset()
            expect(testComponent.value.reset).toHaveBeenCalled()
            expect(testComponent.value.cards.length).toBe(1)
            expect(testComponent.value.cards[0].name).toBe('')
            expect(testComponent.value.cards.length).toBe(1)
            expect(testComponent.value.cards[0].name).toBe('')
        })

        it('should test resetting cards using testResetCards', () => {
            testComponent.value.cards = [
                { id: 1, name: 'The Fool', major: true, img: 'https://example.com/fool.jpg' },
            ]
            testComponent.value.reset()
            expect(testComponent.value.cards.length).toBe(1)
            expect(testComponent.value.cards[0].name).toBe('')
        })

})
