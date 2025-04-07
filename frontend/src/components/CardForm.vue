<template>
    <div v-if="currentTarot" class="edit-form">
      <h4>Tarot</h4>
      <form>
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" class="form-control" id="title"
            v-model="currentTarot.title"
          />
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <input type="text" class="form-control" id="description"
            v-model="currentTarot.description"
          />
        </div>

        <div class="form-group">
          <label><strong>Status:</strong></label>
          {{ currentTarot.published ? "Published" : "Pending" }}
        </div>
      </form>

      <button class="badge badge-primary mr-2"
        v-if="currentTarot.published"
        @click="updatePublished(false)"
      >
        UnPublish
      </button>
      <button v-else class="badge badge-primary mr-2"
        @click="updatePublished(true)"
      >
        Publish
      </button>

      <button class="badge badge-danger mr-2"
        @click="deleteTarot"
      >
        Delete
      </button>

      <button type="submit" class="badge badge-success"
        @click="updateTarot"
      >
        Update
      </button>
      <p>{{ message }}</p>
    </div>

    <div v-else>
      <br />
      <p>Please click on a Tarot...</p>
    </div>
  </template>

  <script>
  import TarotDataService from "../services/TarotDataService";

  export default {
    name: "TarotCard",
    data() {
      return {
        currentTarot: null,
        message: ''
      };
    },
    methods: {
      getTarot(id) {
        TarotDataService.get(id)
          .then(response => {
            this.currentTarot = response.data;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },

      updatePublished(status) {
        var data = {
          id: this.currentTarot.id,
          title: this.currentTarot.title,
          description: this.currentTarot.description,
          published: status
        };

        TarotDataService.update(this.currentTarot.id, data)
          .then(response => {
            console.log(response.data);
            this.currentTarot.published = status;
            this.message = 'The status was updated successfully!';
          })
          .catch(e => {
            console.log(e);
          });
      },

      updateTarot() {
        TarotDataService.update(this.currentTarot.id, this.currentTarot)
          .then(response => {
            console.log(response.data);
            this.message = 'The tutorial was updated successfully!';
          })
          .catch(e => {
            console.log(e);
          });
      },

      deleteTarot() {
        TarotDataService.delete(this.currentTarot.id)
          .then(response => {
            console.log(response.data);
            this.$router.push({ name: "tutorials" });
          })
          .catch(e => {
            console.log(e);
          });
      }
    },
    mounted() {
      this.message = '';
      this.getTarot(this.$route.params.id);
    }
  };
  </script>

  <style>
  .edit-form {
    max-width: 300px;
    margin: auto;
  }
  </style>
