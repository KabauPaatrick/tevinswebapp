import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminPage from '@/views/AdminPage.vue'
import Customers from '@/views/CustomerView.vue'
import Entities from '@/views/EntitiesView.vue'
import Achievements from '@/views/AchievementAdmin.vue'
import Testimonials from  '@/views/TestimonialView.vue'
import Homeview from '@/views/HomePage.vue'
import Solutions from '@/views/SolutionsView.vue'
import LoginPage from '@/views/LoginPage.vue'
import DocumentUpload from '@/views/DocumentUpload.vue'
import Licenses from  '@/views/LicenseAdmin.vue'
import Contact from  '@/views/ContactView.vue'

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
    path:'/contact',
    name:'contact',
    component:Contact

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
    path:'/admin/solutions',
    name:'solutions',
    component:Solutions

  },
  
  {
    path:'/admin/licenses',
    name:'licenses',
    component:Licenses

  },

  {
    path:'/login',
    name:'login',
    component:LoginPage
  },
  {
    path:'/upload',
    name:'DocumentUpload',
    component:DocumentUpload
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
