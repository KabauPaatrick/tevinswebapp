<template>
    <div class="container mt-5">
      <!-- Testimonials Form -->
      <div class="row">
        <div class="col-md-6 col-md-12">
          <div class="card card-testimonial">
            <form @submit.prevent="submitTestimonial" class="form">
              <h2 class="form-title">Create New Testimonial</h2>
              <div class="form-group">
                <label for="author" class="form-label">Author:</label>
                <input type="text" id="author" v-model="testimonial.author" class="form-input" required>
              </div>
              <div class="form-group">
                <label for="position" class="form-label">Position:</label>
                <input type="text" id="position" v-model="testimonial.position" class="form-input" required>
              </div>
              <div class="form-group">
                <label for="content" class="form-label">Content:</label>
                <textarea id="content" v-model="testimonial.content" class="form-input" required></textarea>
              </div>
              <div class="form-group">
                <label for="date" class="form-label">Date:</label>
                <input type="date" id="date" v-model="testimonial.date" class="form-input" required>
              </div>
              <div class="form-group">
                <label for="testimonialImage" class="form-label">Image:</label>
                <input type="file" id="testimonialImage" @change="handleImageUpload" class="form-input" accept="image/*" required>
              </div>
              <div class="form-group">
                <label for="entity" class="form-label">Entity:</label>
                <select v-model="testimonial.entity" id="entity" class="form-input" required>
                  <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}</option>
                </select>
              </div>
              <div class="row mt-3">
                <div class="col-md-12 d-flex justify-content-between">
                  <button type="submit" class="btn btn-primary">Add Testimonial</button>
                  <button type="button" class="btn btn-primary" @click="updateTestimonial(testimonial.id)">Update</button>
                </div>
              </div>
            </form>
          </div>
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

    const fetchEntities = async () => {
      try {
        if (!entitiesFetched.value) {
          const response = await axios.get('http://127.0.0.1:8000/api/entity/entities/');
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

    const updateTestimonialForm = (selectedTestimonial) => {
      testimonial.author = selectedTestimonial.author;
      testimonial.position = selectedTestimonial.position;
      testimonial.content = selectedTestimonial.content;
      testimonial.date = selectedTestimonial.date;
      testimonial.testimonialImage = selectedTestimonial.testimonial_image;
      testimonial.entity = selectedTestimonial.entity;
    };

    const updateTestimonial= ()=>{

    }

    const handleImageUpload = (event) => {
      testimonial.testimonialImage = event.target.files[0];
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
      handleImageUpload,
      updateTestimonial
    };
  }
};
</script>
<style>
.card {
    margin-bottom: 20px;
}
</style>