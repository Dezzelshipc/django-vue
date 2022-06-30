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
            <label for="email">Email</label>
        </td>
    </tr>
    <tr>
        <td>
            <input type="email" v-model="email" id="email">
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
            <button @click="register">Register</button>
        </td>
    </tr>
    <tr style="text-align: right">
        <td>
            <router-link to="/login">
                <button>Back</button>
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
      email: '',
      username: '',
      password: '',
      showPassword: false,
      textResponse: '',
    }
  },
  title() {
    return "Register"
  },
  methods: {
    async register() {
        await axios.post('/api/users/', {
          username: this.username,
          password: this.password,
          email: this.email
        }).then(response => {
          console.log(response)
          this.textResponse = 'Success!'
        }).catch(error => {
          console.log(error)
          this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
          console.log(this.textResponse)
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