<template>
    <div class="AddtoCart">
      <AdminNav />
      <Admintop />
      <AdminProduct />
    </div>
  </template>
  
  <script>
  import AdminNav from '@/components/AdminNav.vue';
  import AdminProduct from '@/components/AdminProduct.vue';
import Admintop from '@/components/Admintop.vue';
  
  export default {
    name: 'AdminProductPage',
    components: {
      AdminNav,
      Admintop,
      AdminProduct,
    }
  };
  </script>
  
  