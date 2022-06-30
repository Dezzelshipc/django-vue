<template>
  <div>
    <input type="radio" v-model="mode" value=0 name="all">
    <label for="all">Все</label>
    <input type="radio" v-model="mode" value=1 name="text">
    <label for="text">Случайный текст</label>
    <input type="radio" v-model="mode" value=2 name="random">
    <label for="random">Случайные слова</label>
    <br>
    {{ listUsers }}
    <table>
        <tr>
            <td>
                Пользователь
            </td>
            <td>
                Скорость
            </td>
        </tr>
        <tr v-for="user in listUsers" v-bind:key="user">
            <td>
                {{ user.username }}
            </td>
            <td>
                {{ user.speed }}
            </td>
        </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            users: '',
            mode: 0,
        }
    },
    title() {
        return "Leaderboards"
    },
    async created() {
        try {
            this.users = await axios.put(`/api/users/all`)
            this.users = this.users.data
        } catch (error) {
            console.log(error.response.data)
        }
    },
    computed: {
        listUsers() {
            let list = []
            for (let index = 0; index < this.users.length; index++) {
                const element = this.users[index]
                let speed = 0
                switch (parseInt( this.mode )) {
                    case 0:
                        speed = element.data.bestSpeed
                        break
                    case 1:
                        speed = element.data.text.bestSpeed
                        break
                    case 2:
                        speed = element.data.random.bestSpeed
                        break
                }
                list.push({
                    username: element.username,
                    speed: speed
                })
            }
            return list.sort((a, b) => {
                return b.speed - a.speed
            })
        }
    },
}
</script>

<style>

</style>