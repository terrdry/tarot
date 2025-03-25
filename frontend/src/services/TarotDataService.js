import http from "../http-common";

class TarotDataService {
    getAll() {
        return http.get("/tarot");
    }
    get(id) {
        return http.get(`/tarot/${id}`);
    }

    create(data) {
        return http.post("/tarot", data);
    }

    update(id, data) {
        return http.put(`/tarot/${id}`, data);
    }

    delete(id) {
        return http.delete(`/tarot/${id}`);
    }

    deleteAll() {
        return http.delete(`/tarot`);
    }

    findByTitle(title) {
        return http.get(`/tarot?title=${title}`);
    }
}

export default new TarotDataService();