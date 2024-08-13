<template>
    <div>
      <AdminNav />
      <div class="container mt-5">
        <!-- Color Form -->
        <div class="card mb-4">
          <div class="card-header">
            <h2 class="mb-0">Create New Color</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="submitBrand" class="form">
              <div class="form-group">
                <label for="title" class="form-label">Title:</label>
                <input type="text" id="title" v-model="brand.title" class="form-control" required />
              </div>
              <div class="row mt-3">
                <div class="col-md-12 d-flex justify-content-between">
                  <button type="submit" class="btn btn-primary">Add Brand</button>
                  <button type="button" class="btn btn-primary" @click="updateBrand(brand.id)">Update</button>
                </div>
              </div>
            </form>
          </div>
        </div>
  
        <!-- Color Table -->
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">Brand List</h2>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th>Title</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(brand, index) in brands" :key="index">
                    <td>{{ brand.title }}</td>
                    <td>
                      <button @click="deleteBrand(brand.id)" class="btn btn-danger mr-2">Delete</button>
                      <button @click="updateBrandForm(brand)" class="btn btn-primary">Update</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { reactive, ref, onMounted } from 'vue';
  import axios from 'axios';
  import AdminNav from '@/components/AdminNav.vue';
  
  export default {
    name: 'BrandPage',
    components: {
      AdminNav,
    },
    setup() {
      const brand = reactive({
        id: '',
        title: '',
      });
  
      const brands = ref([]);
  
      const fetchBrands = async () => {
        try {
          const response = await axios.get('https://kabau.pythonanywhere.com/api/brand/show/');
          brands.value = response.data;
        } catch (error) {
          console.error('Error fetching colors:', error);
        }
      };
  
      const deleteBrand = async (id) => {
        try {
          await axios.delete(`https://kabau.pythonanywhere.com/api/brand/${id}/delete/`);
          fetchBrands();
        } catch (error) {
          console.error('Error deleting color:', error);
        }
      };
  
      const updateBrandForm = (selectedBrand) => {
        brand.id = selectedBrand.id;
        brand.title = selectedBrand.title;
      };
  
      const clearForm = () => {
        brand.id = '';
        brand.title = '';
      };
  
      const updateBrand = async (id) => {
        try {
          const response = await axios.put(`https://kabau.pythonanywhere.com/api/brand/${id}/update/`, {
            title: brand.title,
          });
  
          console.log(response.data);
          clearForm();
          
        } catch (error) {
          console.error('Error updating brand:', error);
        }
      };
  
      const submitBrand= async () => {
        try {
          const response = await axios.post('https://kabau.pythonanywhere.com/api/brand/create/', {
            title: brand.title,
          });
  
          console.log(response.data);
          clearForm();
          fetchBrands ();
        } catch (error) {
          console.error('Error submitting brands:', error);
        }
      };
  
      onMounted(() => {
        fetchBrands ();
      });
  
      return {
        brand,
        brands,
        submitBrand,
        deleteBrand,
        updateBrandForm,
        updateBrand ,
      };
    },
  };
  </script>
  
  <style scoped>
  .card {
    margin-bottom: 20px;
  }
  </style>
  