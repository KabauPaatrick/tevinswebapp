import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminPage from '@/views/AdminPage.vue'
import Customers from '@/views/CustomerView.vue'
import Entities from '@/views/EntitiesView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPage
  },
  {
    path:'/admin/customers',
    name:'customers',
    component:Customers
  },
  {
    path:'/admin/entities',
    name:'entities',
    component:Entities
  },
  {
    path:'/admin/achievements',
    name:'achievements',
    component:Achievements
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
