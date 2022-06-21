<template>
  <div>
    <router-view v-if="isLogin && !dev"></router-view>
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
  title() {
    return "App Page"
  },
  data() {
    return {
      check: false,
      items: [
        {label: 'Home', icon: 'pi pi-fw pi-home', to: '/home' },
        {label: 'Write', icon: 'pi pi-fw pi-pencil', to: '/write'},
        {label: 'User', icon: 'pi pi-fw pi-user', to: '/user'},
        {label: 'Logout', icon: 'pi pi-fw pi-sign-out', to: '/logout'}
      ],
      dev: true, // Только для разработки
    }
  },
  updated() {
    if (!this.dev) {
      if (!localStorage.getItem('usernameW') && this.$route.path !== '/register') {
        this.$router.push('/login')
      } else if (localStorage.getItem('usernameW') && (this.$route.path === '/login' || this.$route.path === '/register')) {
        this.$router.push('/home')
      }
    }
  },
  created() {
    if (!this.dev) {
      if (!localStorage.getItem('usernameW')) {
        this.$router.push('/login')
      }
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
}

@import url('~bootstrap/dist/css/bootstrap.css');
</style>
