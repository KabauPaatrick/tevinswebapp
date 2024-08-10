<template>
  <div>
    <AdminNav />
    <h1 class="text-center mb-4">Admin Dashboard</h1>
    <div class="container mt-5" >
      <div class="main-card">
        <div class="card-body">
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
            <div class="col-md-6">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">Manage Solutions</h5>
                  <p class="card-text">Manage solutions view content and layout.</p>
                  <router-link :to="{ name: 'solutions' }" class="btn btn-primary">Go to Solutions</router-link>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">Manage Licenses</h5>
                  <p class="card-text">Manage license view content and layout.</p>
                  <router-link :to="{ name: 'licenses' }" class="btn btn-primary">Go to Licenses</router-link>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">View Orders</h5>
                  <p class="card-text">View Customer Orders</p>
                  <router-link :to="{ name: 'OrdersPage' }" class="btn btn-primary">View Customer Orders</router-link>
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
import AdminNav from '@/components/AdminNav.vue';

export default {
  name: 'NewAdminNPage',
  components: {
    AdminNav,
  },
};
</script>

<style scoped>
body {
  padding: 10px;
  bottom: 0;
  height: 100%;
}

h1 {
  color: black;
}

h5 {
  color: black;
}

.main-card {
  padding: 20px;
  border-radius: 8px;
  max-width: 1800px;
  text-align: left;
  gap: 10px;
}

.card-body {
  color: black;
}

.card {
  margin-bottom: 20px;
  background: #cacbd5;
  color: black;
}

.btn {
  background: orangered;
  border: none;
}

.btn:hover {
  background: #3a6ea5;
}

</style>
