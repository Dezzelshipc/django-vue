<template>
  <div>
    <h2>Top results</h2>
    <!--    {{ listUsers }}-->
    <br>
    <div class="modeTable">
      <div class="modeTableElement">
        <RadioButton name="tableMode" value="0" v-model="mode" />
        <h4>All</h4>
      </div>
      <div class="modeTableElement">
        <RadioButton name="tableMode" value="1" v-model="mode"/>
        <h4>Text</h4>
      </div>
      <div class="modeTableElement">
        <RadioButton name="tableMode" value="2" v-model="mode"/>
        <h4>Words</h4>
      </div>
    </div>
    <br>
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
import RadioButton from 'primevue/radiobutton';

export default {
  components: {
    RadioButton,
  },
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
        switch (parseInt(this.mode)) {
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

<style scoped>
.table {
  width: 100%;
  border: none;
  border-collapse: separate;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 10px;
}

.table thead th {
  font-weight: bold;
  text-align: left;
  border: none;
  padding: 10px 15px;
  background: rgba(237, 237, 237, 0.5);
  font-size: 14px;
  border-top: 1px solid rgba(221, 221, 221, 0.5);
}

.table tr th:first-child, .table tr td:first-child {
  border-left: 1px solid rgba(221, 221, 221, 0.5);
}

.table tr th:last-child, .table tr td:last-child {
  border-right: 1px solid rgba(221, 221, 221, 0.5);
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
  background: rgba(248, 248, 248, 0.5);
}

.table tbody tr:last-child td {
  border-bottom: 1px solid rgba(221, 221, 221, 0.5);
}

.table tbody tr:last-child td:first-child {
  border-radius: 0 0 0 10px;
}

.table tbody tr:last-child td:last-child {
  border-radius: 0 0 10px 0;
}
.modeTable {
  display: flex;
  justify-content: center;
}
.modeTableElement {
  width: 80px;
}
</style>