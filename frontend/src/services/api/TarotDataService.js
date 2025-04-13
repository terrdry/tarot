import http from "../../http-common";

class TarotDataService {
    getAll() {
        return http.get("/cards");
    }
    get(id) {
        return http.get('/cards/read/'+id);
    }
    post(data) {
        return http.post('/cards/add', data);
    }
    create(data) {
        const response = http.post("/cards/add", data);
        return response
    }

    update(id, data) {
        return http.put(`/cards/update/${id}`, data);
    }

    delete(id) {
        return http.i('/cards/delete/'+id);
    }

    //     deleteAll() {
    //         return http.delete(`/tarot`);
    //     }

    //     findByTitle(title) {
    //         return http.get(`/tarot?title=${title}`);
    //     }
}

export default new TarotDataService();
