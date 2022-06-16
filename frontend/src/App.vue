<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      check: false,
    }
  },
  updated() {
    if (!localStorage.getItem('usernameW') && this.$route.path !== '/register') {
      this.$router.push('/login')
    } else if (localStorage.getItem('usernameW') && (this.$route.path === '/login' || this.$route.path === '/register')) {
      this.$router.push('/home')
    }
  },
  created() {
    if (!localStorage.getItem('usernameW')) {
      this.$router.push('/login')
    }
  },
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

@import url('~bootstrap/dist/css/bootstrap.css');
</style>
