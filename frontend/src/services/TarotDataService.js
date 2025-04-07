import http from "../http-common";

class TarotDataService {
    getAll() {
        return http.get("/cards");
    }
    get() {
        return http.get('/cards/read');
    }
    post(data) {
        return http.post('/cards/add', data);
    }
    create() {
        return http.post("/cards/add");
    }

    //     update(id, data) {
    //         return http.put(`/tarot/${id}`, data);
    //     }

    //     delete(id) {
    //         return http.delete(`/tarot/${id}`);
    //     }

    //     deleteAll() {
    //         return http.delete(`/tarot`);
    //     }

    //     findByTitle(title) {
    //         return http.get(`/tarot?title=${title}`);
    //     }
}

export default new TarotDataService();
