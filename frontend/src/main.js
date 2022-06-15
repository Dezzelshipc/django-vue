import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import PrimeVue from 'primevue/config'
import 'bootstrap'

const app = createApp(App)

app.use(router)
app.use(PrimeVue)

app.mount('#app')