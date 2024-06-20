<template>
  <nav>
    <div class="nav-container">
      <h1>E-Commerce</h1>
      <div class="nav-items">
        <ul>
          <router-link to="/">Home</router-link>
          <router-link to="/">Resources</router-link>
          <router-link to="/">Support</router-link>
          <router-link to="/">Country</router-link>
          <router-link to="/products">Shop</router-link>
        </ul>
      </div>
    </div>
  </nav>
</template>
  
<script>
export default {
  name: 'NavBar',
  data() {
    return {
      isMenuOpen: false,
      showMenuIcon: false
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    checkScreenSize() {
      this.showMenuIcon = window.innerWidth <= 500;
    },
  },
  mounted() {
    // Check screen size on mount
    this.checkScreenSize();
    // Listen for window resize events
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeUnmount() {
    // Remove resize event listener
    window.removeEventListener('resize', this.checkScreenSize);
  }
};
</script>

<style scoped>
nav {
  background: #d5d5d5;
  width: 100vw;
  height: 75px;
  top: 0;
  padding: 20px;
}

.nav-container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: black;
  margin-top: 5px;
}

.nav-container h1 {
  font-size: 25px;
  font-weight: 700;
}

nav ul {
  display: flex;
  gap: 70px;
  list-style: none;
  align-items: center;
}

a {
  text-decoration: none;
  color: black;
}


</style>
