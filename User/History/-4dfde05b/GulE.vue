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
  }
  .card {
    /* Styles for individual testimonial cards */
  }
  .position {
    /* Styles for position text */
  }
  </style>
  