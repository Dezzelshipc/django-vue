<template>
  <div>
    {{ users }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            users: '',
        }
    },
    async created() {
        try {
            this.users = await axios.put(`/api/users/all`)
            console.log(this.users)
            this.users = this.users.data
        } catch (error) {
            console.log(error.response.data)
        }
    },
}
</script>

<style>

</style>