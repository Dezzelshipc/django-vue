<template>
  <div id="app">
    <router-view v-if="isLogin"></router-view>
    <div v-else>
      <header>
        <TabMenu :model="items" />
      </header>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import TabMenu from 'primevue/tabmenu';


export default {
  components: {
    TabMenu,
  },
  name: 'App',
  data() {
    return {
      check: false,
      items: [
        {label: 'Home', icon: 'pi pi-fw pi-home', to: '/home' },
        {label: 'Write', icon: 'pi pi-fw pi-pencil', to: '/write'},
        {label: 'User', icon: 'pi pi-fw pi-user', to: 'user'},
      ],
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
  computed: {
    isLogin() {
      return this.$route.path === '/login' || this.$route.path === '/register'
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

@import url('~bootstrap/dist/css/bootstrap.css');
</style>
