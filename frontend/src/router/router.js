import { createRouter, createWebHashHistory } from 'vue-router'
import WritePage from '../components/WritePage'
import LoginUser from '../components/LoginUser'
import Home from '../components/vHome'
import RegisterUser from '../components/RegisterUser'
import UserPage from '../components/UserPage'
import LogoutPage from '../components/LogoutPage'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/' },
        { path: '/login', component: LoginUser },
        { path: '/register', component: RegisterUser },
        { path: '/write', component: WritePage },
        { path: '/home', component: Home },
        { path: '/user', component: UserPage },
        { path: '/logout', component: LogoutPage },
    ]
})

export default router