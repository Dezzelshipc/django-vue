<template>
  <v-vanta effect="fog" :options="options"></v-vanta>
  <div>
    <nav>
      <TabMenu :model="items" />
    </nav>
    <div class="content">
      <router-view v-if="isLogin && !dev"></router-view>
      <div v-else>
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import TabMenu from 'primevue/tabmenu'
import VVanta from 'vue-vanta';


export default {
  components: {
    TabMenu,
    VVanta,
  },
  name: 'App',
  title() {
    return "App Page"
  },
  data() {
    return {
      options: {
        el: "#boddy",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 1000.00,
        minWidth: 200.00,
        highlightColor: 0x96ff,
        midtoneColor: 0xa400ff,
        lowlightColor: 0x5b4f9d,
        baseColor: 0xffffff,
      },
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
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.content {
  max-width: 1000px;
  min-height: 300px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 15px;
  margin-top: 20px;
  margin-bottom: 100px;
  background-color: rgba(255, 255, 255, .25);
  backdrop-filter: blur(15px);
  padding: 50px;
}
.p-tabmenu .p-tabmenu-nav{
  border-radius: 15px;
  margin-bottom: 30px;
  background-color: rgba(255, 255, 255, .25);
  backdrop-filter: blur(15px);
  margin-top: 30px;
}
.p-tabmenu .p-tabmenu-nav .p-tabmenuitem .p-menuitem-link {
  border-radius: 15px;
}
nav {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}
@import url('~bootstrap/dist/css/bootstrap.css');
</style>
