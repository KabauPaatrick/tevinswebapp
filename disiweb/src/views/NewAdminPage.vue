<template>
    <div class="NewAdminPage">
      <AdminNav />
    </div>
  </template>
  
  <script>
  import AdminNav from '@/components/AdminNav.vue';
  
  export default {
    name: 'NewAdminNPage', // Correct component name
    components: {
      AdminNav,
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles if necessary */
  </style>
  