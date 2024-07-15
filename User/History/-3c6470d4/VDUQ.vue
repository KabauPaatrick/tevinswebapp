<template>
    <div class="container mt-5">
      <h1 class="text-center mb-4">Admin Dashboard</h1>
      <div class="row">
        <div class="col-md-4">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Manage Customers</h5>
              <p class="card-text">Manage customer data and interactions.</p>
              <router-link :to="{ name: 'customers' }" class="btn btn-primary">Go to Customers</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Manage Entities</h5>
              <p class="card-text">Manage entities and their details.</p>
              <router-link :to="{ name: 'entities' }" class="btn btn-primary">Go to Entities</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Manage Achievements</h5>
              <p class="card-text">Manage achievements and milestones.</p>
              <router-link :to="{ name: 'achievements' }" class="btn btn-primary">Go to Achievements</router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Manage Testimonials</h5>
              <p class="card-text">Manage customer testimonials and reviews.</p>
              <router-link :to="{ name: 'testimonials' }" class="btn btn-primary">Go to Testimonials</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Manage Home View</h5>
              <p class="card-text">Manage home view content and layout.</p>
              <router-link :to="{ name: 'homeview' }" class="btn btn-primary">Go to Home View</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    // Add necessary logic here
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  .card {
    margin-bottom: 20px;
  }
  </style>
  