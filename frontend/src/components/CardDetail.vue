<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control"
          placeholder="Search by title"
          v-model="title"
        />
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button" @click="searchTitle">
            Search
          </button>
        </div>
      </div>
    </div>

    <div class="col-md-6">
      <h4>Tarot Card List</h4>
      <ul class="list-group">
        <li
          class="list-group-item"
          v-for="(tarot, id) in tarots"
          :key="id"
        >
          {{ tarot.name }}

        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllTarots">
        Remove All
      </button>
    </div>

    <div class="col-md-6">
      <div v-if="currentTarot">
        <h4>Tarot</h4>
        <p><strong>Current route path:</strong> {{ route.fullPath }}</p>
        <div>
          <label><strong>Title:</strong></label> {{ currentTarot.title }}
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentTarot.description }}
        </div>
        <div>
          <label><strong>Status:</strong></label> {{ currentTarot.published ? "Published" : "Pending" }}
        </div>

        <router-link :to="`/tarots/${currentTarot.id}`" class="badge badge-warning">Edit</router-link>
      </div>
      <div v-else>
        <br />
        <p>Please click on a Tarot...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import tarotDataService from "../services/TarotDataService";

const tarots = ref([]);
const currentTarot = ref(null);
const currentIndex = ref(-1);
const title = ref("");

const route = useRoute();

const retrieveTarots = async () => {
  try {
    tarots.value = await tarotDataService.getAll()
    console.log(tarots.value)
  } catch (error) {
    console.error('Error fetching items:', error)
  }
};

const refreshList = () => {
  retrieveTarots();
  currentTarot.value = null;
  currentIndex.value = -1;
};

const setActiveTarot = (tarot, index) => {
  currentTarot.value = tarot;
  currentIndex.value = tarot ? index : -1;
};

const removeAllTarots = () => {
  tarotDataService.deleteAll()
    .then((response) => {
      console.log(response.data);
      refreshList();
    })
    .catch((e) => {
      console.log(e);
    });
};

const searchTitle = () => {
  tarotDataService.findByTitle(title.value)
    .then((response) => {
      tarots.value = response.data;
      setActiveTarot(null);
      console.log(response.data);
    })
    .catch((e) => {
      console.log(e);
    });
};

onMounted(() => {
  retrieveTarots();
});
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>
