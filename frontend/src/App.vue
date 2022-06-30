<template>
  <div>
    <v-vanta effect="fog" :options="options"></v-vanta>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/home"><h4>MusicType</h4></router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/home"><h5>Home</h5></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/write"><h5>Write</h5></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/leaderboard"><h5>Leaderboard</h5></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/user"><h5>User</h5></router-link>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <router-link class="nav-link" to="/logout"><h5>Login/Logout</h5></router-link>
          </form>
        </div>
      </div>
    </nav>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>

import VVanta from 'vue-vanta';


export default {
  components: {
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
      // items: [
      //   {label: 'Home', icon: 'pi pi-fw pi-home', to: '/home' },
      //   {label: 'Write', icon: 'pi pi-fw pi-pencil', to: '/write'},
      //   {label: 'User', icon: 'pi pi-fw pi-user', to: '/user'},
      //   {label: 'Logout', icon: 'pi pi-fw pi-sign-out', to: '/logout'}
      // ],
    }
  },
  created() {
    if (!localStorage.getItem('usernameW')) {
      this.$router.push('/login')
    } else if (localStorage.getItem('usernameW') && (this.isLogin)) {
      this.$router.push('/home')
    }
  },
  computed: {
    isLogin() {
      return this.$route.path === '/login' || this.$route.path === '/register' || this.$route.path === '/'
    }
  },
  watch: {
    $route() {
      if (!localStorage.getItem('usernameW') && this.$route.path !== '/register') {
        this.$router.push('/login')
      } else if (localStorage.getItem('usernameW') && (this.isLogin)) {
        this.$router.push('/home')
      }
    }
  }
}
</script>

<style>
@import url('~bootstrap/dist/css/bootstrap.css');

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
  box-shadow: 0 0 10px rgba(180, 180, 180, 0.5);
}


nav {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  background-color: rgba(255, 255, 255, .25);
  backdrop-filter: blur(15px);

}

.navbar {
  border-radius: 15px;
  margin-bottom: 30px;
  box-shadow: 0 0 10px rgba(180, 180, 180, 0.5);
  padding-right: 20px;
  padding-left: 20px;
}
.nav-link {
  color: whitesmoke;
}
.navbar-brand {
  color: whitesmoke;
  text-shadow: 2px 4px 3px rgba(0,0,0,0.3);
}
</style>
