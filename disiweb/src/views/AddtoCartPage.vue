<template>
    <div class="AddtoCart">
      <NavBar />
      <AddtoCart />
    </div>
  </template>
  
  <script>
  import NavBar from '@/components/NavBar.vue';
  import AddtoCart from '@/components/AddtoCart.vue';
  
  export default {
    name: 'AddtoCartPage',
    components: {
      NavBar,
      AddtoCart,
    }
  };
  </script>
  
  