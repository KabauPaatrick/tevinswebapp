<template>
  <nav>
    <div class="nav-container">
      <h1>E-Commerce</h1>
      <div class="nav-items">
        <ul :class="{ 'open': isMenuOpen }">
          <router-link to="/">Home</router-link>
          <router-link to="/">Resources</router-link>
          <router-link to="/">Support</router-link>
          <router-link to="/">Country</router-link>
          <router-link to="/products">Shop</router-link>
        </ul>
      </div>
      <div class="menu-icon" @click="toggleMenu" v-if="showMenuIcon">
        <div :class="{ 'change': isMenuOpen }" class="bar1"></div>
        <div :class="{ 'change': isMenuOpen }" class="bar2"></div>
        <div :class="{ 'change': isMenuOpen }" class="bar3"></div>
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
      this.showMenuIcon = window.innerWidth <= 768;
      if (window.innerWidth > 768) {
        this.isMenuOpen = false;
      }
    },
  },
  mounted() {
    this.checkScreenSize();
    window.addEventListener('resize', this.checkScreenSize);
  },
  beforeUnmount() {
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
}

.nav-container h1 {
  font-size: 25px;
  font-weight: 700;
}

.nav-items ul {
  display: flex;
  gap: 70px;
  list-style: none;
  align-items: center;
}

a {
  text-decoration: none;
  color: black;
}

.menu-icon {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.bar1, .bar2, .bar3 {
  width: 30px;
  height: 5px;
  background-color: black;
  margin: 3px 0;
  transition: 0.4s;
}

.change.bar1 {
  transform: rotate(-45deg) translate(-9px, 6px);
}

.change.bar2 {
  opacity: 0;
}

.change.bar3 {
  transform: rotate(45deg) translate(-8px, -8px);
}

@media (max-width: 768px) {
  .nav-items ul {
    display: none;
    flex-direction: column;
    gap: 20px;
    position: absolute;
    top: 75px;
    left: 0;
    width: 100%;
    background: #d5d5d5;
    padding: 20px 0;
  }

  .nav-items ul.open {
    display: flex;
  }

  .menu-icon {
    display: flex;
  }

  a:hover{
    color: red;
  }
}
</style>
