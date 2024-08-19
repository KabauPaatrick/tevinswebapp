<template>
    <div class="newbody">
        <AdminNav />
        <AdminHome />
    </div>
  </template>
  
  <script>
  import AdminHome from '@/components/AdminHome.vue';
  import AdminNav from '@/components/AdminNav.vue';
  
  export default {
    name: 'AdminPage',
    components: {
      AdminHome,
      AdminNav
    },
  };
  </script>