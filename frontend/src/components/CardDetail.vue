<template>
    <div class="list row">
      <div class="col-md-8">
        <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="Search by title"
            v-model="title"/>
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button"
              @click="searchTitle"
            >
              Search
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <h4>Tarot Card List</h4>
        <ul class="list-group">
          <li class="list-group-item"
            :class="{ active: index == currentIndex }"
            v-for="(tarot, index) in tarots"
            :key="index"
            @click="setActiveTarot(tarot, index)"
          >
            {{ tarot.title }}
          </li>
        </ul>
  
        <button class="m-3 btn btn-sm btn-danger" @click="removeAllTarots">
          Remove All
        </button>
      </div>
      <div class="col-md-6">
        <div v-if="currentTarot">
          <h4>Tarot</h4>
          <div>
            <label><strong>Title:</strong></label> {{ currentTarot.title }}
          </div>
          <div>
            <label><strong>Description:</strong></label> {{ currentTarot.description }}
          </div>
          <div>
            <label><strong>Status:</strong></label> {{ currentTarot.published ? "Published" : "Pending" }}
          </div>
  
          <router-link :to="'/tarots/' + currentTarot.id" class="badge badge-warning">Edit</router-link>
        </div>
        <div v-else>
          <br />
          <p>Please click on a Tarot...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import TarotDataService from "../services/TarotDataService";
  
  export default {
    name: "TarotCard-list",
    data() {
      return {
        cards: [],
        currentTarot: null,
        currentIndex: -1,
        title: ""
      };
    },
    methods: {
      retrieveCards() {
        TarotDataService.getAll()
          .then(response => {
            this.tarots = response.data;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },
  
      refreshList() {
        this.retrieveTarots();
        this.currentTarot = null;
        this.currentIndex = -1;
      },
  
      setActiveTarot(tarot, index) {
        this.currentTarot = tarot;
        this.currentIndex = tarot ? index : -1;
      },
  
      removeAllTarots() {
        TarotDataService.deleteAll()
          .then(response => {
            console.log(response.data);
            this.refreshList();
          })
          .catch(e => {
            console.log(e);
          });
      },
      
      searchTitle() {
        TarotDataService.findByTitle(this.title)
          .then(response => {
            this.tarots = response.data;
            this.setActiveTarot(null);
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      }
    },
    mounted() {
      this.retrieveTarots();
    }
  };
  </script>
  
  <style>
  .list {
    text-align: left;
    max-width: 750px;
    margin: auto;
  }
  </style>