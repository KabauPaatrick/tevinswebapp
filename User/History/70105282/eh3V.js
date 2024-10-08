import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminPage from '@/views/AdminPage.vue'
import Customers from '@/views/CustomerView.vue'
import Entities from '@/views/EntitiesView.vue'
import Achievements from '@/views/AchievementAdmin.vue'
import Testimonials from  '@/views/TestimonialView.vue'
import Homeview from '@/views/HomePage.vue'

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
  {
    path:'/admin/testimonials',
    name:'testimonials',
    component:Testimonials
  },
  {
    path:'/admin/homeview',
    name:'homeview',
    component:Homeview
  },
  {
    path:'/admin/'
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
