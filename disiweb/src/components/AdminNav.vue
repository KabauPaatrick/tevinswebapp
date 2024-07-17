<template>
    <aside class="sidebar">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
      <div class="sidebar-header">
        <img src="@/assets/images/headphones.png" alt="logo" />
        <h2>E-commerce</h2>
      </div>
      <ul class="sidebar-links">
        <li>
          <router-link :to="{ name: 'admin' }">
            <span class="material-symbols-outlined">dashboard</span>Dashboard
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'customers' }">
            <span class="material-symbols-outlined">person</span>Customers
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'entities' }">
            <span class="material-symbols-outlined">groups</span>Entities
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'achievements' }">
            <span class="material-symbols-outlined">trophy</span>Achievements
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'testimonials' }">
            <span class="material-symbols-outlined">forum</span>Testimonials
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'homeview' }">
            <span class="material-symbols-outlined">move_up</span>Homeview
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'solutions' }">
            <span class="material-symbols-outlined">lightbulb</span>Solutions
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'licenses' }">
            <span class="material-symbols-outlined">contract</span>Licences
          </router-link>
        </li>
        <li>
          <router-link :to="{name: 'OrdersPage'}">
            <span class="material-symbols-outlined">shopping_cart</span>Orders
          </router-link>
        </li>
        <li>
          <router-link :to="{name: 'AdminProductPage'}">
            <span class="material-symbols-outlined">shopping_bag</span>Products
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'login' }">
            <span class="material-symbols-outlined">logout</span>Logout
          </router-link>
        </li>
      </ul>
    </aside>
  </template>
  
  <script>
  export default {
    name: 'AdminNav'
  };
  </script>

<style scoped>
/* Importing Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  min-height: 100vh;
  background: #F0F4FF;
}

.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 75px;
  display: flex;
  overflow-x: hidden;
  flex-direction: column;
  background: #cacbd5;
  padding: 25px 20px;
  transition: all 0.4s ease;
  z-index: 1;
}

.sidebar:hover {
  width: 260px;
}

.sidebar .sidebar-header {
  display: flex;
  align-items: center;
}

.sidebar .sidebar-header img {
  width: 42px;
  margin-left: -15px;
}

.sidebar .sidebar-header h2 {
  color: black;
  font-size: 1.25rem;
  font-weight: 600;
  white-space: nowrap;
  margin-left: 13px;
}

.sidebar-links h4 {
  color: #fff;
  font-weight: 500;
  white-space: nowrap;
  margin: 10px 0;
  position: relative;
}

.sidebar-links h4 span {
  opacity: 0;
}

.sidebar:hover .sidebar-links h4 span {
  opacity: 1;
}

.sidebar-links {
  list-style: none;
  margin-top: 20px;
  height: 80%;
  overflow-y: auto;
  scrollbar-width: none;
}

.sidebar-links li a {
  display: flex;
  align-items: center;
  gap: 0 20px;
  color: black;
  font-weight: 500;
  white-space: nowrap;
  padding: 15px 10px;
  text-decoration: none;
  transition: 0.2s ease;
}

.sidebar-links li a:hover {
  color: #161a2d;
  background: #fff;
  border-radius: 4px;
}

</style>