<template>
  <div id="app">
    <div>
      <button @click="check = !check">asdads</button>
      {{ check }}
    </div>
    <TasksHandler />

    <WritePage />
  </div>
</template>

<script>
import TasksHandler from './components/TasksHandler.vue'
import WritePage from './components/WritePage.vue'


export default {
  name: 'App',
  components: {
    TasksHandler,
    WritePage,
  },
  data() {
    return {
      check: false,
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
