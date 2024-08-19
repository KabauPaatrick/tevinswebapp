<template>
    <div class="EditProduct">
      <AdminNav />
      <Admintop />
      <EditProduct />
    </div>
  </template>
  
  <script>
  import AdminNav from '@/components/AdminNav.vue';
  import Admintop from '@/components/Admintop.vue';
  import EditProduct from '@/components/EditProduct.vue';
  
  export default {
    name: 'EditProductPage',
    components: {
      AdminNav,
      Admintop,
      EditProduct,
    }
  };
  </script>
  
  