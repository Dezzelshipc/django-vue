<template>
  <div>
    <h1>
        {{ username }}
    </h1>
    <div>
        <h2>
            Лучшая скорость: {{ response.bestSpeed }} знаков в секунду.
        </h2>
    </div>
    <br>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            response: [],
        }
    },
    async created() {
        this.username = localStorage.getItem("usernameW")
        try {
            this.response = await axios.get(`/api/users/${this.username}`)
            this.response = this.response.data.data
            console.log(this.response)
        } catch (error) {
            console.log(error.response.data)
        }
    },
}
</script>

<style>

</style>