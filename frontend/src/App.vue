<template>
  <v-vanta effect="fog" :options="options"></v-vanta>
  <div class="boddy" id="boddy">
    <TabMenu :model="items" />
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
/*body {*/
/*  background-image: url('https://images.saymedia-content.com/.image/t_share/MTc4NzM1OTc4MzE0MzQzOTM1/how-to-create-cool-website-backgrounds-the-ultimate-guide.png');*/
/*  background-size: 100%;*/
/*}*/
.content {
  width: 1000px;
  min-height: 300px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 30px;
  margin-top: 100px;
  margin-bottom: 100px;
  background-color: rgba(255, 255, 255, .25);
  backdrop-filter: blur(8px);
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
