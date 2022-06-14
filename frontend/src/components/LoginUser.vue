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
    <tr style="text-align: center; white-space: pre;">
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
            await axios.put(`/api/users/`, {
                username: this.username,
                password: this.password,
            }).then(response =>{
                console.log(response)

                localStorage.setItem('usernameW', this.username)
                this.textResponse = 'Success!'
                this.$router.push('/home')
            }).catch(error => {
                console.log(error)
                this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
                console.log(this.textResponse)
                
                // this.textResponse = 'Username or password error'
            })
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