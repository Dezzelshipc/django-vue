<template>
  <div class="content">
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
body {
  background-image: url('https://images.saymedia-content.com/.image/t_share/MTc4NzM1OTc4MzE0MzQzOTM1/how-to-create-cool-website-backgrounds-the-ultimate-guide.png');
  background-size: 100%;
}
.content {
  width: 1000px;
  min-height: 300px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 30px;
  margin-top: 100px;
  margin-bottom: 100px;
  background-color: rgba(255, 255, 255, .25);
  backdrop-filter: blur(5px);
  padding: 50px;
}
.p-tabmenu .p-tabmenu-nav{
  border-radius: 30px;
  margin-bottom: 30px;
}
.p-tabmenu .p-tabmenu-nav .p-tabmenuitem .p-menuitem-link {
  border-radius: 30px;
}
@import url('~bootstrap/dist/css/bootstrap.css');
</style>
