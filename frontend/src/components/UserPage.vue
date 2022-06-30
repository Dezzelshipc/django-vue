<template>
  <div>
    <h1>
        {{ username }}
    </h1>
    <div>
        <h2>
            Лучшая скорость: {{ response.bestSpeed }} знаков в секунду.
        </h2>
    </div>
    <br>
    <Chart type="line" :data="basicData" />
  </div>
</template>

<script>
import Chart from 'primevue/chart'

import axios from 'axios'

export default {
    components: {
        Chart
    },
    data() {
        return {
            response: [],
            basicData: {
				labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				datasets: [
					{
						label: 'Случайные слова',
						backgroundColor: '#42A5F5',
						data: []
					},
					{
						label: 'Случайный текст',
						backgroundColor: '#9CCC65',
						data: []
					}
				]
            },
        }
    },
    async created() {
        this.username = localStorage.getItem("usernameW")
        try {
            this.response = await axios.get(`/api/users/${this.username}`)
            this.response = this.response.data.data
            this.basicData.datasets[0].data = this.response.text.last.map(element => { return element.speed })
            this.basicData.datasets[1].data = this.response.random.last.map(element => { return element.speed })
            console.log(this.basicData)
        } catch (error) {
            console.log(error.response.data)
        }
    },
}
</script>

<style>

</style>