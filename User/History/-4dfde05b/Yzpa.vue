<template>
    <div class="testimonials">
      <h2>Testimonials</h2>
      <div class="testimonial-cards">
        <div v-for="testimonial in testimonials" :key="testimonial.id" class="card">
          <p class="position">{{ testimonial.position }}</p>
          <p>{{ testimonial.author }}</p>
          <p>{{ testimonial.content }}</p>
          <span>- {{ testimonial.author }}, {{ testimonial.position }}</span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  
  export default {
    setup() {
      const testimonials = ref([]);
  
      const fetchTestimonials = async () => {
        try {
          const response = await fetch('http://127.0.0.1:8000/api/testimonials/show/');
          if (!response.ok) {
            throw new Error('Failed to fetch testimonials');
          }
          const data = await response.json();
          testimonials.value = data;
        } catch (error) {
          console.error('Error fetching testimonials:', error.message);
        }
      };
  
      onMounted(fetchTestimonials);
  
      return {
        testimonials,
      };
    },
  };
  </script>
  
  <style scoped>
  .testimonials {
    /* Styles for the testimonials section */
  }
  
  .testimonial-cards {
    /* Styles for the container of testimonial cards */
    display: flex;
    flex-wrap: wrap;
  }
  
  .card {
    /* Styles for individual testimonial cards */
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    margin: 10px;
    width: calc(33.33% - 20px); /* Adjust as needed */
  }
  
  .position {
    /* Styles for position text */
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  /* Additional styles */
  p {
    margin: 5px 0;
  }
  
  span {
    font-style: italic;
    color: #777;
  }
  </style>
  