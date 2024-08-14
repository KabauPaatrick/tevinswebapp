<template>
  <nav>
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
          <li><router-link to="/signup">
            <div class="profile-icon">
              <span class="material-symbols-outlined">person</span>Admin
            </div>
          </router-link></li>
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
import { ref, onMounted, onBeforeUnmount } from 'vue';

export default {
  name: 'NavBar',
  setup() {
    const isMenuOpen = ref(false);
    const showMenuIcon = ref(false);

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    const checkScreenSize = () => {
      showMenuIcon.value = window.innerWidth <= 768;
      if (window.innerWidth > 768) {
        isMenuOpen.value = false;
      }
    };

    onMounted(() => {
      checkScreenSize();
      window.addEventListener('resize', checkScreenSize);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', checkScreenSize);
    });

    return {
      isMenuOpen,
      showMenuIcon,
      toggleMenu,
    };
  },
};
</script>

<style scoped>
*{
  z-index: 1000;
}

nav {
  background: #d5d5d5;
  width: 100%;
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
  transition: all 0.3s ease;
}

.nav-items ul li {
  list-style: none;
}

a {
  text-decoration: none;
  color: black;
}

a:hover {
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

.profile-icon:hover {
  background: #989998;
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

  a:hover {
    color: red;
  }
}
</style>
