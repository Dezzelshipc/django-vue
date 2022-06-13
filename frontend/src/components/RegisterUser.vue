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
      email: '',
      username: '',
      password: '',
      showPassword: false,
      textResponse: '',
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('/api/users/', {
          username: this.username,
          password: this.password,
          email: this.email
        })

        switch (response.status) {
          case 201:
            this.textResponse = 'Success!'
            break
          default:
            console.log(response.data)
            this.textResponse = 'Error'
        }
      } catch(error) {
        console.log(error)

        switch (error.response.status) {
          case 201:
            this.textResponse = 'Success!'
            break
          case 400:
            this.textResponse = 'Registration error'
            break
          case 409:
            this.textResponse = 'Username already exists'
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