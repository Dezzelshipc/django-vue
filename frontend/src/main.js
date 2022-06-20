import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import PrimeVue from 'primevue/config'
import 'bootstrap'


import 'primevue/resources/themes/md-light-deeppurple/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons



const app = createApp(App)

app.use(router)
app.use(PrimeVue)



app.mount('#app')
