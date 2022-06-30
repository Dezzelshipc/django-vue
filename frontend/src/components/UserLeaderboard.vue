<template>
  <div>
    <input type="radio" v-model="mode" value=0 name="all">
    <label for="all">Все</label>
    <input type="radio" v-model="mode" value=1 name="text">
    <label for="text">Случайный текст</label>
    <input type="radio" v-model="mode" value=2 name="random">
    <label for="random">Случайные слова</label>
    <br>
    <h2>Top results</h2>
    <!--    {{ listUsers }}-->
    <table class="table">
      <thead>
      <tr>
        <th>
          Пользователь
        </th>
        <th>
          Скорость
        </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in listUsers" v-bind:key="user">
        <td>
          {{ user.username }}
        </td>
        <td>
          {{ user.speed }}
        </td>
      </tr>
      </tbody>
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
.table {
  width: 100%;
  border: none;
  border-collapse: separate;
  background-color: white;
  border-radius: 10px;
}
.table thead th {
  font-weight: bold;
  text-align: left;
  border: none;
  padding: 10px 15px;
  background: #EDEDED;
  font-size: 14px;
  border-top: 1px solid #ddd;
}
.table tr th:first-child, .table tr td:first-child {
  border-left: 1px solid #ddd;
}
.table tr th:last-child, .table tr td:last-child {
  border-right: 1px solid #ddd;
}
.table thead tr th:first-child {
  border-radius: 10px 0 0 0;
}
.table thead tr th:last-child {
  border-radius: 0 10px 0 0;
}
.table tbody td {
  text-align: left;
  border: none;
  padding: 10px 15px;
  font-size: 14px;
  vertical-align: top;
}
.table tbody tr:nth-child(even) {
  background: #F8F8F8;
}
.table tbody tr:last-child td{
  border-bottom: 1px solid #ddd;
}
.table tbody tr:last-child td:first-child {
  border-radius: 0 0 0 10px;
}
.table tbody tr:last-child td:last-child {
  border-radius: 0 0 10px 0;
}
</style>