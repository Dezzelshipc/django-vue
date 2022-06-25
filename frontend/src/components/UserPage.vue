<template>
  <div>
    {{ bestSpeed }}
    <br>
    {{ username }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            bestSpeed: 0,
            telegram: '',
            responseText: '',
        }
    },
    async created() {
        this.username = localStorage.getItem("usernameW")
        try {
            const response = await axios.get(`/api/users/${this.username}`)
            this.bestSpeed = response.data['bestSpeed']
            this.telegram = response.data['telegram']
        } catch (error) {
            console.log(error.response.data)
        }
    },
}
</script>

<style>

</style>