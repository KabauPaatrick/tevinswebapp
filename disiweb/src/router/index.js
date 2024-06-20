import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AdminPage from '@/views/AdminPage.vue';
import Customers from '@/views/CustomerView.vue';
import Entities from '@/views/EntitiesView.vue';
import Achievements from '@/views/AchievementAdmin.vue';
import Testimonials from '@/views/TestimonialView.vue';
import HomePage from '@/views/HomePage.vue';
import Solutions from '@/views/SolutionsView.vue';
import LoginPage from '@/views/LoginPage.vue';
import DocumentUpload from '@/views/DocumentUpload.vue';
import Licenses from '@/views/LicenseAdmin.vue';
import Contact from '@/views/ContactView.vue';
import CartPage from '@/views/CartPage.vue';
import ItemPage from '@/views/ItemPage.vue';
import ProductsPage from '@/views/ProductsPage.vue';
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '@/views/AboutView.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPage
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact
  },
  {
    path: '/admin/customers',
    name: 'customers',
    component: Customers
  },
  {
    path: '/admin/entities',
    name: 'entities',
    component: Entities
  },
  {
    path: '/admin/achievements',
    name: 'achievements',
    component: Achievements
  },
  {
    path: '/admin/testimonials',
    name: 'testimonials',
    component: Testimonials
  },
  {
    path: '/admin/homeview',
    name: 'homeview',
    component: HomePage
  },
  {
    path: '/admin/solutions',
    name: 'solutions',
    component: Solutions
  },
  {
    path: '/admin/licenses',
    name: 'licenses',
    component: Licenses
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/upload',
    name: 'DocumentUpload',
    component: DocumentUpload
  },
  {
    path: '/cartpage',
    name: 'Cartpage',
    component: CartPage
  },
  {
    path: '/cart',
    name: 'Itempage',
    component: ItemPage
  },
  {
    path: '/products',
    name: 'ProductPage',
    component: ProductsPage
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
