<template>
  <div>
      <button @click="logout">Log out</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.clear('usernameW')
      this.$router.push('/login')
    }
  },
}
</script>

<style>

</style>