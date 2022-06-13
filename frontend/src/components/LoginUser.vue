<template>
<table class="center">
    <tbody style="text-align: left">
    <tr>
        <td>
            <label for="usr">Username</label>
        </td>
    </tr>
    <tr>
        <td>
            <input type="text" v-model="username" id="usr">
        </td>
    </tr>
    <tr>
        <td>
            <label for="pass">Password</label>
        </td>
    </tr>
    <tr>
        <td>
            <input :type="showPassword ? 'text' : 'password'" v-model="password" id="pass">
        </td>
    </tr>
    <tr>
        <td>
            <input type="checkbox" v-model="showPassword" title="show pass" id="showpass">
            <label for="showpass">Show Password</label>
        </td>
    </tr>
    <tr style="text-align: right">
        <td>
            <button @click="login">Log in</button>
        </td>
    </tr>
    <tr style="text-align: right">
        <td>
            <router-link to="/register">
                <button>Register</button>
            </router-link>
        </td>
    </tr>
    <tr style="text-align: center">
        <td>
            {{ textResponse }}
        </td>
    </tr>
    </tbody>
</table>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            showPassword: false,
            username: '',
            password: '',
            textResponse: '',
        }
    },
    methods: {
        async login() {

            try {
                const response = await axios.put(`/api/users/`, {
                    username: this.username,
                    password: this.password,
                })

                switch (response.status) {
                    case 200:
                        localStorage.setItem('usernameW', this.username)
                        this.textResponse = 'Success!'
                        this.$router.push('/home')
                        break
                    default:
                        console.log(response.data)
                        this.textResponse = 'Error'
                }
            } catch(error) {
                console.log(error)

                switch (error.response.status) {
                    case 401:
                        this.textResponse = 'Username or password error'
                        break
                    default:
                        this.textResponse = error
                }
            }
        }
    },
}
</script>

<style>
.center {
    position: relative;
    margin: auto;
}
</style>