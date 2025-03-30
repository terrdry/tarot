<!-- <script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style> -->
<template>
  <div id="app">
    <main>
      <CardList />
    </main> 
  </div>

</template>

<script setup>
import CardList from './components/CardList.vue'


// import { ref } from 'vue'

// reactive state
// const message = ref('Hello, Vue!')

// Functions that mutate state and trigger updates
// const updateMessage = () => {
  // message.value = 'You clicked the button!'

// lifecyle hooks

</script>
<!-- 
<style scoped>
button {
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
</style> -->
