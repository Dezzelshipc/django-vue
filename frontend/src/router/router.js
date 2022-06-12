import { createRouter, createWebHashHistory } from 'vue-router'
import TaskHandler from '../components/TasksHandler'
import WritePage from '../components/WritePage'
import LoginUser from '../components/LoginUser'
import Home from '../components/vHome'
import RegisterUser from '../components/RegisterUser'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/', component: TaskHandler },
        { path: '/login', component: LoginUser },
        { path: '/register', component: RegisterUser },
        { path: '/write', component: WritePage },
        { path: '/home', component: Home },
    ]
})

export default router