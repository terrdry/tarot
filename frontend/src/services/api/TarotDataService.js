import http from "../../http-common";

/**
 * Service class for interacting with the Tarot API.
 */
class TarotDataService {
    /**
     * Fetches all tarot cards.
     * @returns {Promise} A promise that resolves to the response of the GET request.
     */
    getAll() {
        return http.get("/cards");
    }

    /**
     * Fetches a specific tarot card by its ID.
     * @param {string|number} id - The ID of the tarot card to retrieve.
     * @returns {Promise} A promise that resolves to the response of the GET request.
     */
    get(id) {
        return http.get('/cards/read/'+id);
    }

    /**
     * Submits new tarot card data to the server.
     * @param {Object} data - The data of the tarot card to add.
     * @returns {Promise} A promise that resolves to the response of the POST request.
     */
    post(data) {
        return http.post('/cards/add', data);
    }

    /**
     * Creates a new tarot card entry on the server.
     * @param {Object} data - The data of the tarot card to create.
     * @returns {Promise} A promise that resolves to the response of the POST request.
     */
    create(data) {
        return http.post("/cards/add", data);
    }

    /**
     * Updates an existing tarot card entry on the server.
     * @param {string|number} id - The ID of the tarot card to update.
     * @param {Object} data - The updated data for the tarot card.
     * @returns {Promise} A promise that resolves to the response of the POST request.
     */
    update(id, data) {
        return http.post(`/cards/update/${id}`, data);
    }

    /**
     * Deletes a tarot card entry from the server.
     * @param {string|number} id - The ID of the tarot card to delete.
     * @returns {Promise} A promise that resolves to the response of the POST request.
     */
    delete(id) {
        return http.post('/cards/delete/'+id);
    }
}

/**
 * Exports a singleton instance of the TarotDataService class.
 * This service is used to interact with the Tarot API for fetching or managing tarot-related data.
 */
export default new TarotDataService();
