<template>
    <div class="EditProduct">
      <AdminNav />
      <EditProduct />
    </div>
  </template>
  
  <script>
  import AdminNav from '@/components/AdminNav.vue';
  import EditProduct from '@/components/EditProduct.vue';
  
  export default {
    name: 'EditProductPage',
    components: {
      AdminNav,
      EditProduct,
    }
  };
  </script>
  
  