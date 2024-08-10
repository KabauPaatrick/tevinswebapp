<template>
    <div class="sidebar">
        <link rel="stylesheet" 
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <div class="sidebar-header">
            <img src="@/assets/images/headphones.png" alt="logo" />
            <h2>E-commerce</h2>
        </div>
    </div>
</template>

<script>
export default {
  name: 'TestNav'
};
</script>

<style scoped>
.sidebar {
  position: fixed;
  height: 100%;
  width: 300px;
  background: #11224e;
  padding: 15px;
  z-index: 99;
  color: #fff;
  display: flex;
  flex-direction: column;
  text-align: left
}

.sidebar .sidebar-header img {
  width: 42px;
  margin-left: -15px;
}
</style>