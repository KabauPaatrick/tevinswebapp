<template>
    <div>
      <AdminNav />
      <div class="container mt-5">
        <!-- Category Form -->
        <div class="card mb-4">
          <div class="card-header">
            <h2 class="mb-0">Create New Category</h2>
          </div>
          <div class="card-body">
            <form @submit.prevent="submitCategory" class="form">
              <div class="form-group">
                <label for="title" class="form-label">Title:</label>
                <input type="text" id="title" v-model="category.title" class="form-control" required />
              </div>
              <div class="row mt-3">
                <div class="col-md-12 d-flex justify-content-between">
                  <button type="submit" class="btn btn-primary">Add Category</button>
                  <button type="button" class="btn btn-primary" @click="updateCategory(category.id)">Update</button>
                </div>
              </div>
            </form>
          </div>
        </div>
  
        <!-- Category Table -->
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">Category List</h2>
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
                  <tr v-for="(category, index) in categories" :key="index">
                    <td>{{ category.title }}</td>
                    <td>
                      <button @click="deleteCategory(category.id)" class="btn btn-danger mr-2">Delete</button>
                      <button @click="updateCategoryForm(category)" class="btn btn-primary">Update</button>
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
    name: 'CategoryPage',
    components: {
      AdminNav,
    },
    setup() {
      const category = reactive({
        id: '',
        title: '',
      });
  
      const categories = ref([]);
  
      const fetchCategories = async () => {
        try {
          const response = await axios.get('https://kabau.pythonanywhere.com/api/category/list/');
          categories.value = response.data;
        } catch (error) {
          console.error('Error fetching categories:', error);
        }
      };
  
      const deleteCategory = async (id) => {
        try {
          await axios.delete(`https://kabau.pythonanywhere.com/api/category/${id}/delete/`);
          fetchCategories();
        } catch (error) {
          console.error('Error deleting category:', error);
        }
      };
  
      const updateCategoryForm = (selectedCategory) => {
        category.id = selectedCategory.id;
        category.title = selectedCategory.title;
      };
  
      const clearForm = () => {
        category.id = '';
        category.title = '';
      };
  
      const updateCategory = async (id) => {
        try {
          const response = await axios.put(`https://kabau.pythonanywhere.com/api/category/${id}/update/`, {
            title: category.title,
          });
  
          console.log(response.data);
          clearForm();
          fetchCategories();
        } catch (error) {
          console.error('Error updating category:', error);
        }
      };
  
      const submitCategory = async () => {
        try {
          const response = await axios.post('https://kabau.pythonanywhere.com/api/category/create/', {
            title: category.title,
          });
  
          console.log(response.data);
          clearForm();
          fetchCategories();
        } catch (error) {
          console.error('Error submitting category:', error);
        }
      };
  
      onMounted(() => {
        fetchCategories();
      });
  
      return {
        category,
        categories,
        submitCategory,
        deleteCategory,
        updateCategoryForm,
        updateCategory,
      };
    },
  };
  </script>
  
  <style scoped>
  .card {
    margin-bottom: 20px;
  }
  </style>
  