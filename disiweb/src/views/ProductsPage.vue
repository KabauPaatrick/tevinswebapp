<template>
    <div class="cart">
      <!-- <NavBar /> -->
      <Products />
    </div>
  </template>
  
  <script>
  // import NavBar from '@/components/NavBar.vue';
  import Products from '@/components/ProductsList.vue';
  
  export default {
    name: 'ProductsPage', // Correct component name
    components: {
      // NavBar,
      Products
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles if necessary */
  </style>
  