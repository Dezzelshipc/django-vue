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
    title() {
        return this.username
    },
    data() {
        return {
            username: '',
            response: [],
            basicData: {
				labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				datasets: [
					{
						label: 'Случайные слова',
						backgroundColor: 'rgba(66,165,245,0.5)',
            borderColor: 'rgb(66,165,245)',
						data: [],
            fill: true,
            tension: .4,
					},
					{
						label: 'Случайный текст',
						backgroundColor: 'rgba(154,101,204,0.5)',
            borderColor: 'rgb(154,101,204)',
						data: [],
            fill: true,
            tension: .4,
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