<template>
    <div>
      <h1 class="text-center mb-4">Admin Dashboard</h1>
      <div class="container mt-5">
        <div class="card" style="background-color: forestgreen;">
          <div class="card-body">
            <div class="row">
              <div class="col-md-4">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Customers</h5>
                    <p class="card-text text-white">Manage customer data and interactions.</p>
                    <router-link :to="{ name: 'customers' }" class="btn btn-primary">Go to Customers</router-link>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Entities</h5>
                    <p class="card-text text-white">Manage entities and their details.</p>
                    <router-link :to="{ name: 'entities' }" class="btn btn-primary">Go to Entities</router-link>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Achievements</h5>
                    <p class="card-text text-white">Manage achievements and milestones.</p>
                    <router-link :to="{ name: 'achievements' }" class="btn btn-primary">Go to Achievements</router-link>
                  </div>
                </div>
              </div>
            </div>
            <div class="row mt-4">
              <div class="col-md-6">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Testimonials</h5>
                    <p class="card-text text-white">Manage customer testimonials and reviews.</p>
                    <router-link :to="{ name: 'testimonials' }" class="btn btn-primary">Go to Testimonials</router-link>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Home View</h5>
                    <p class="card-text text-white">Manage home view content and layout.</p>
                    <router-link :to="{ name: 'homeview' }" class="btn btn-primary">Go to Home View</router-link>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="card bg-transparent border-0">
                  <div class="card-body">
                    <h5 class="card-title text-white">Manage Solutions</h5>
                    <p class="card-text text-white">Manage solutions view content and layout.</p>
                    <router-link :to="{ name: 'solutions' }" class="btn btn-primary">Go to Solutions</router-link>
                  </div>
                </div>
              </div>
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
  