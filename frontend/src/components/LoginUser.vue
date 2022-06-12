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
    </tbody>
</table>
</template>

<script>
export default {
    data() {
        return {
            showPassword: false,
            username: '',
            password: '',
        }
    },
    methods: {
        login() {
            this.$router.push('/home')
        }
    }
}
</script>

<style>
.center {
    position: relative;
    margin: auto;
}
</style>