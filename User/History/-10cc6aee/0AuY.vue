<template>
    <div class="container mt-5">
      <!-- Testimonials Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Testimonial</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="submitTestimonial" class="form">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="author" class="form-label">Author:</label>
                  <input type="text" id="author" v-model="testimonial.author" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="position" class="form-label">Position:</label>
                  <input type="text" id="position" v-model="testimonial.position" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="content" class="form-label">Content:</label>
                  <textarea id="content" v-model="testimonial.content" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="date" class="form-label">Date:</label>
                  <input type="date" id="date" v-model="testimonial.date" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="testimonialImage" class="form-label">Image:</label>
                  <input type="file" id="testimonialImage" @change="handleImageUpload" class="form-control" accept="image/*" required>
                </div>
                <div class="form-group">
                  <label for="entity" class="form-label">Entity:</label>
                  <select v-model="testimonial.entity" id="entity" class="form-control" required>
                    <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Add Testimonial</button>
                <button type="button" class="btn btn-primary" @click="updateTestimonial(selectedTestimonial)">Update</button>
              </div>
            </div>
          </form>
        </div>
      </div>
  
      <!-- Testimonial Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Testimonial List</h2>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Author</th>
                  <th>Position</th>
                  <th>Content</th>
                  <th>Date</th>
                  <th>Image</th>
                  <th>Entity</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(testimonial, index) in testimonials" :key="index">
                  <td>{{ testimonial.author }}</td>
                  <td>{{ testimonial.position }}</td>
                  <td>{{ testimonial.content }}</td>
                  <td>{{ testimonial.date }}</td>
                  <td>
                    <img :src="testimonial.image" alt="Testimonial Image" style="max-width: 100px; max-height: 100px;">
                  </td>
                  <td>{{ getEntityName(testimonial.entity) }}</td>
                  <td>
                    <button @click="deleteTestimonial(testimonial.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateTestimonialForm(testimonial)" class="btn btn-primary">Update</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { reactive, onMounted, ref } from 'vue';
  import axios from 'axios';
  
  export default {
    setup() {
      const testimonial = reactive({
        author: '',
        position: '',
        content: '',
        date: '',
        testimonialImage: null,
        entity: '',
      });
  
      const testimonials = ref([]);
      const entities = ref([]);
      const entitiesFetched = ref(false);
      const selectedTestimonial = ref(null); 
  
      const fetchEntities = async () => {
        try {
          if (!entitiesFetched.value) {
            const response = await axios.get('http://127.0.0.1:8000/api/entity/show/');
            entities.value = response.data;
            entitiesFetched.value = true;
          }
        } catch (error) {
          console.error('Error fetching entities:', error);
        }
      };
  
      const fetchTestimonials = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/testimonials/show/');
          testimonials.value = response.data;
        } catch (error) {
          console.error('Error fetching testimonials:', error);
        }
      };
  
      const submitTestimonial = async () => {
        try {
          const formData = new FormData();
          formData.append('author', testimonial.author);
          formData.append('position', testimonial.position);
          formData.append('content', testimonial.content);
          formData.append('date', testimonial.date);
          formData.append('testimonial_image', testimonial.testimonialImage);
          formData.append('entity', testimonial.entity);
  
          const response = await axios.post('http://127.0.0.1:8000/api/testimonials/create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
  
          console.log(response.data);
  
          // Clear form fields after successful submission
          Object.keys(testimonial).forEach(key => {
            testimonial[key] = '';
          });
  
          // Refresh testimonials list
          fetchTestimonials();
        } catch (error) {
          console.error('Error submitting testimonial:', error);
        }
      };
  
      const deleteTestimonial = async (id) => {
        try {
          await axios.delete(`http://127.0.0.1:8000/api/testimonials/${id}/delete`);
          fetchTestimonials();
        } catch (error) {
          console.error('Error deleting testimonial:', error);
        }
      };
  
      const updateTestimonialForm = (selectedTestimonialData) => {
      // Populate form fields with selected testimonial data
      testimonial.author = selectedTestimonialData.author;
      testimonial.position = selectedTestimonialData.position;
      testimonial.content = selectedTestimonialData.content;
      testimonial.date = selectedTestimonialData.date;
      testimonial.testimonialImage = selectedTestimonialData.testimonial_image; // Check property name
      testimonial.entity = selectedTestimonialData.entity;

      // Store selected testimonial
      selectedTestimonial.value = selectedTestimonialData;
    };

    const updateTestimonial = async () => {
      // Check if a testimonial is selected
      if (!selectedTestimonial.value) {
        console.error('No testimonial selected for update.');
        return;
      }

      try {
        // Construct form data
        const formData = new FormData();
        formData.append('author', testimonial.author);
        formData.append('position', testimonial.position);
        formData.append('content', testimonial.content);
        formData.append('date', testimonial.date);
        formData.append('testimonial_image', testimonial.testimonialImage);
        formData.append('entity', testimonial.entity);

        // Make PUT request to update testimonial
        const response = await axios.put(`http://127.0.0.1:8000/api/testimonials/${selectedTestimonial.value.id}/update/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        console.log(response.data);

        // Clear form fields after successful update
        Object.keys(testimonial).forEach(key => {
          testimonial[key] = '';
        });

        // Refresh testimonials list
        fetchTestimonials();
      } catch (error) {
        console.error('Error updating testimonial:', error);
      }
    };
      const handleImageUpload = (event) => {
        testimonial.testimonialImage = event.target.files[0];
      };
  
      const getEntityName = (entityId) => {
        const entity = entities.value.find(entity => entity.id === entityId);
        return entity ? entity.name : '';
      };
  
      onMounted(() => {
        fetchEntities();
        fetchTestimonials();
      });
  
      return {
        testimonial,
        testimonials,
        entities,
        submitTestimonial,
        deleteTestimonial,
        updateTestimonialForm,
        updateTestimonial,
        handleImageUpload,
        getEntityName
      };
    }
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  .card {
    margin-bottom: 20px;
  }
  </style>
  