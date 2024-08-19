<template>
  <nav>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    />
    <div class="nav-container">
      <div class="nav-items">
        <div class="dropdown-icon" @click="toggleDropdown">
          <span class="material-symbols-outlined menu-icon">menu</span>
          <ul class="dropdown-menu" v-show="isDropdownOpen" ref="dropdownMenu">
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
              <router-link :to="{ name: 'Location' }">
                <span class="material-symbols-outlined">pin_drop</span>Location
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'OrdersPage' }">
                <span class="material-symbols-outlined">shopping_cart</span>Orders
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'CategoryPage' }">
                <span class="material-symbols-outlined">category</span>Categories
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'ColorsPage' }">
                <span class="material-symbols-outlined">palette</span>Colors
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'BrandPage' }">
                <span class="material-symbols-outlined">branding_watermark</span>Branding
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'AddProduct' }">
                <span class="material-symbols-outlined">add</span>Add Product
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'AdminProductPage' }">
                <span class="material-symbols-outlined">shopping_bag</span>Products
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'login' }">
                <span class="material-symbols-outlined">logout</span>Logout
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'MainNav',
  data() {
    return {
      isDropdownOpen: false,
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    handleClickOutside(event) {
      const dropdownMenu = this.$refs.dropdownMenu;
      const dropdownIcon = this.$el.querySelector('.dropdown-icon');
      if (dropdownMenu && !dropdownMenu.contains(event.target) && !dropdownIcon.contains(event.target)) {
        this.isDropdownOpen = false;
      }
    },
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  },
};
</script>

  
<style scoped>
@media (max-width: 1000px) {
  a {
    color: black;
    text-decoration: none;
  }
  
  nav {
    background: #d5d5d5;
    width: 1fr;
    height: 70px;
    top: 0;
    left: 0;
    padding: 0 50px;
    z-index: 11;
  }
  
  .nav-container {
    height: 100%;
    display: flex;
    justify-content: end;
    align-items: center;
    color: black;
  }
  
  .nav-items {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .material-symbols-outlined {
    font-variation-settings:
      'FILL' 0,
      'wght' 400,
      'GRAD' 0,
      'opsz' 24;
  }
  
  .dropdown-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 20px;
    padding: 2px;
    cursor: pointer;
  }
  
  .dropdown-icon:hover {
    background: rgba(255, 255, 255, 0.1);
  }
  
  .dropdown-menu {
    z-index: 11;
    position: absolute;
    min-width: 200px;
    top: 50px;
    right: 20px;
    background: #cacbd5;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    list-style: none;
    padding: 10px 0;
    font-size: 15px;
  }
  
  .dropdown-menu li {
    padding: 10px 20px;
    border-radius: 5px;
  }
  
  .dropdown-menu li:hover {
    background: white;
  }
  
  .dropdown-menu li a {
    text-decoration: none;
    color: #000;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 20px;
  }
  
  #nav-text {
    display: none;
  }
}
</style>

  