<template>
    <div class="AddtoCart">
      <AdminNav />
      <AdminProduct />
    </div>
  </template>
  
  <script>
  import AdminNav from '@/components/AdminNav.vue';
  import AdminProduct from '@/components/AdminProduct.vue';
  
  export default {
    name: 'AdminProductPage',
    components: {
      AdminNav,
      AdminProduct,
    }
  };
  </script>
  
  