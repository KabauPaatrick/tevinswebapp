<template>
  <nav :class="{ 'scrolled': hasScrolled }">
    <link rel="stylesheet" 
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <div class="nav-container">
      <h1>Byden Constructions Limited</h1>
      <div class="nav-items">
        <ul :class="{ 'open': isMenuOpen }">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/">Resources</router-link></li>
          <li><router-link to="/">Support</router-link></li>
          <li><router-link to="/">Country</router-link></li>
          <li><router-link to="/products">Products/services</router-link></li>
          <li><router-link to="/signup">Admin
            <!-- <div class="profile-icon">
              <span class="material-symbols-outlined">person</span>Admin
            </div> -->
          </router-link></li>
        </ul>
      </div>
      <button>Contact Us</button>
      <div class="menu-icon" @click="toggleMenu" v-if="showMenuIcon">
        <div :class="{ 'change': isMenuOpen }" class="bar1"></div>
        <div :class="{ 'change': isMenuOpen }" class="bar2"></div>
        <div :class="{ 'change': isMenuOpen }" class="bar3"></div>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';

export default {
  name: 'NavBar',
  setup() {
    const isMenuOpen = ref(false);
    const showMenuIcon = ref(false);
    const hasScrolled = ref(false);

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    const checkScreenSize = () => {
      showMenuIcon.value = window.innerWidth <= 768;
      if (window.innerWidth > 768) {
        isMenuOpen.value = false;
      }
    };

    const handleScroll = () => {
      hasScrolled.value = window.scrollY > 50;
    };

    onMounted(() => {
      checkScreenSize();
      window.addEventListener('resize', checkScreenSize);
      window.addEventListener('scroll', handleScroll);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', checkScreenSize);
      window.removeEventListener('scroll', handleScroll);
    });

    return {
      isMenuOpen,
      showMenuIcon,
      toggleMenu,
      hasScrolled,
    };
  },
};
</script>

<style scoped>
nav {
  background: transparent;
  color: black;
  width: 100%;
  height: 75px;
  top: 0;
  left: 0;
  padding: 20px;
  position: fixed;
  z-index: 1000;
  transition: background-color 0.3s ease, color 0.3s ease;
}

nav.scrolled {
  background: #1769FF;
  color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.nav-container {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center; /* Align items to the center */
  color: inherit;
}

.nav-container h1 {
  font-size: 18px;
  font-weight: 700;
  color: white;
  transition: color 0.2s ease;
  margin: 0; /* Ensure no margin */
  cursor: pointer;
}

nav.scrolled .nav-container h1 {
  color: white;
}

.nav-items ul {
  display: flex;
  gap: 50px;
  font-weight: 600;
  list-style: none;
  align-items: center;
  transition: all 0.3s ease;
  margin: 0; /* Ensure no margin */
}

.nav-items ul li {
  list-style: none;
}

a {
  text-decoration: none;
  color: white;
  display: flex;
  align-items: center; /* Align links vertically */
}

a:hover {
  color: #1769FF;
}

nav.scrolled a {
  color: white;
}
nav.scrolled a:hover {
  color: black;
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

.profile-icon:hover {
  background: #989998;
}

button {
  font-size: 1em;
  background-color: #1769FF;
  color: white;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  font-weight: 600;
  height: 40px;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background: #033496;
  color: white;
}

nav.scrolled button {
  background-color: white;
  color: #1769FF;
}
nav.scrolled button:hover {
  background-color: white;
  color: #1769FF;
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
  background-color: white;
  margin: 3px 0;
  transition: 0.4s;
}

nav.scrolled .bar1{
  background-color: white;
}

nav.scrolled .bar2{
  background-color: white;
}

nav.scrolled .bar3{
  background-color: white;
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
  nav {
    background: #1769FF;
  }

  button {
    background-color: white;
    color: #1769FF;
  }

  .nav-items ul {
    display: none;
    flex-direction: column;
    gap: 0; /* Remove gap between li elements */
    position: absolute;
    top: 75px;
    left: 0;
    width: 100%;
    background: #1769FF;
    padding: 0; /* Adjust padding as needed */
  }

  .nav-items ul li {
    width: 100%; /* Make li take up full width */
  }

  a {
    display: flex; /* Use flexbox to center content */
    justify-content: center; /* Center content horizontally */
    align-items: center; /* Center content vertically */
    text-align: center; /* Center text inside a */
    color: white;
    padding: 10px 20px;
    width: 100%;
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  a:hover {
    background-color: white; /* Change background to white on hover */
    color: #1769FF; /* Change text color to #1769FF on hover */
  }

  nav.scrolled a {
    color: white;
  }

  nav.scrolled a:hover {
    background-color: white;
    color: #1769FF;
  }

  .nav-items ul.open {
    display: flex;
  }

  .menu-icon {
    display: flex;
  }
}



</style>
