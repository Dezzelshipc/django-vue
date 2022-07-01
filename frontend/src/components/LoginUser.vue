<template>
<table class="center">
    <tbody style="text-align: left">
    <tr>
        <td>
            <label for="usr"><h6>Username</h6></label>
        </td>
    </tr>
    <tr>
        <td>
            <InputText class="p-inputtext" type="text" v-model="username" id="usr"/>
        </td>
    </tr>
    <tr>
        <td>
            <label for="pass"><h6>Password</h6></label>
        </td>
    </tr>
    <tr>
        <td>
            <InputText class="p-inputtext" :type="showPassword ? 'text' : 'password'" v-model="password" id="pass"/>
        </td>
    </tr>
    <tr>
        <td>
            <Checkbox class="align-middle" v-model="showPassword" title="show pass" id="showpass" :binary="true"  />
            <label for="showpass"><h6>&nbsp;Show Password</h6></label>
        </td>
    </tr>
    <tr style="text-align: right">
        <td>
            <Button @click="login">Log in</Button>
        </td>
    </tr>
    <tr style="text-align: right">
        <td>
            <router-link to="/register">
                <Button>Register</Button>
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
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Checkbox from 'primevue/checkbox'

import axios from 'axios'

export default {
    components: {
        Button,
        InputText,
        Checkbox
    },
    data() {
        return {
            showPassword: false,
            username: '',
            password: '',
            textResponse: '',
        }
    },
    title() {
        return "Login"
    },
    methods: {
        async login() {
            await axios.put(`/api/users/`, {
                username: this.username,
                password: this.password,
            }).then(() =>{
                localStorage.setItem('usernameW', this.username)
                this.textResponse = 'Success!'
                this.$router.push('/home')
            }).catch(error => {
                console.log(error)
                this.textResponse = Object.values( error.response.data ).map(x => x[0]).join('\r\n')
                if (this.textResponse.length > 5) {
                    this.textResponse = "Server error"
                }
                console.log(this.textResponse)
                
                // this.textResponse = 'Username or password error'
            })
        }
    },
}
</script>

<style scoped>
.center {
    position: relative;
    margin: auto;
}

.p-inputtext {
    padding: 4px;
}

router-link {
    text-decoration: none;
}
</style>