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
          <div class="profile-icon" v-if="!showMenuIcon">
            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-user-filled" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
              <path d="M12 2a5 5 0 1 1 -5 5l.005 -.217a5 5 0 0 1 4.995 -4.783z" stroke-width="0" fill="currentColor" />
              <path d="M14 14a5 5 0 0 1 5 5v1a2 2 0 0 1 -2 2h-10a2 2 0 0 1 -2 -2v-1a5 5 0 0 1 5 -5h4z" stroke-width="0" fill="currentColor" />
            </svg>
          </div>
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

a:hover{
  color: red;
}

.profile-icon {
  display: flex;
  cursor: pointer;
  height: 40px;
  width: 40px;
  justify-content: center;
  align-items: center;
  border-radius: 25px;
}

.profile-icon:hover{
  background: #989998;
}

.profile-icon svg {
  /* Your custom styles for the SVG */
  width: 55px;
  height: 55px;
  /* Additional styling as needed */
}

/* Example: Change fill color on hover */
.profile-icon svg:hover {
  
}


.menu-icon {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.bar1, .bar2, .bar3 {
  width: 30px;
  height: 4px;
  border-radius: 5px;
  background-color: black;
  margin: 3px 0;
  transition: 0.4s;
}

.change.bar1 {
  transform: rotate(-45deg) translate(-9px, 5px);
}

.change.bar2 {
  opacity: 0;
}

.change.bar3 {
  transform: rotate(45deg) translate(-9px, -5px);
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
