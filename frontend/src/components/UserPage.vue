<template>
  <div>
    {{ bestSpeed }}
    <br>
    {{ username }}
    <br>
    <input type="text" placeholder="@telegram" v-model="telegram">
    <button @click="put_telegram">Save Telegram</button>
    <br>
    {{ responseText }}
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
    methods: {
        async put_telegram() {
            if (!this.telegram.startsWith("@")) {
                this.responseText = 'Not starts with @ symbol'
                return
            }
            await axios.post(`/api/users/${this.username}`, {
                telegram: this.telegram
            }).then(response => {
                console.log(response)
                this.telegram = response.data['telegram']
                this.responseText = 'Success!'
            }).catch(error => {
                console.log(error)
                this.responseText = error.response.data
            })  
        }
    },
}
</script>

<style>

</style>