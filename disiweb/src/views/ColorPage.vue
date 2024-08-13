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
            <form @submit.prevent="submitColor" class="form">
              <div class="form-group">
                <label for="title" class="form-label">Title:</label>
                <input type="text" id="title" v-model="color.title" class="form-control" required />
              </div>
              <div class="row mt-3">
                <div class="col-md-12 d-flex justify-content-between">
                  <button type="submit" class="btn btn-primary">Add Color</button>
                  <button type="button" class="btn btn-primary" @click="updateColor(color.id)">Update</button>
                </div>
              </div>
            </form>
          </div>
        </div>
  
        <!-- Color Table -->
        <div class="card">
          <div class="card-header">
            <h2 class="mb-0">Color List</h2>
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
                  <tr v-for="(color, index) in colors" :key="index">
                    <td>{{ color.title }}</td>
                    <td>
                      <button @click="deleteColor(color.id)" class="btn btn-danger mr-2">Delete</button>
                      <button @click="updateColorForm(color)" class="btn btn-primary">Update</button>
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
    name: 'ColorPage',
    components: {
      AdminNav,
    },
    setup() {
      const color = reactive({
        id: '',
        title: '',
      });
  
      const colors = ref([]);
  
      const fetchColors = async () => {
        try {
          const response = await axios.get('https://kabau.pythonanywhere.com/api/color/show/');
          colors.value = response.data;
        } catch (error) {
          console.error('Error fetching colors:', error);
        }
      };
  
      const deleteColor = async (id) => {
        try {
          await axios.delete(`https://kabau.pythonanywhere.com/api/color/${id}/delete/`);
          fetchColors();
        } catch (error) {
          console.error('Error deleting color:', error);
        }
      };
  
      const updateColorForm = (selectedColor) => {
        color.id = selectedColor.id;
        color.title = selectedColor.title;
      };
  
      const clearForm = () => {
        color.id = '';
        color.title = '';
      };
  
      const updateColor = async (id) => {
        try {
          const response = await axios.put(`https://kabau.pythonanywhere.com/api/color/${id}/update/`, {
            title: color.title,
          });
  
          console.log(response.data);
          clearForm();
          fetchColors();
        } catch (error) {
          console.error('Error updating color:', error);
        }
      };
  
      const submitColor = async () => {
        try {
          const response = await axios.post('https://kabau.pythonanywhere.com/api/color/create/', {
            title: color.title,
          });
  
          console.log(response.data);
          clearForm();
          fetchColors();
        } catch (error) {
          console.error('Error submitting color:', error);
        }
      };
  
      onMounted(() => {
        fetchColors();
      });
  
      return {
        color,
        colors,
        submitColor,
        deleteColor,
        updateColorForm,
        updateColor,
      };
    },
  };
  </script>
  
  <style scoped>
  .card {
    margin-bottom: 20px;
  }
  </style>
  