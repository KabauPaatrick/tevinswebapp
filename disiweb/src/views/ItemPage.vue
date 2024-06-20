<template>
    <div class="cart">
      <NavBar />
      <CartItem />
    </div>
  </template>
  
  <script>
  import NavBar from '@/components/NavBar.vue';
  import CartItem from '@/components/CartItem.vue';
  
  export default {
    name: 'ItemPage', // Correct component name
    components: {
      NavBar,
      CartItem
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles if necessary */
  </style>
  