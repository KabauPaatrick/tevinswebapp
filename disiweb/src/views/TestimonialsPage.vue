<template>
  <div v-if="testimonials.length > 0" class="testimonials">
    <h1>Testimonials</h1>
    <div class="testimonial-cards">
      <div v-for="testimonial in testimonials" :key="testimonial.id" class="t-cards">
        <img class="t-image" :src="testimonial.testimonial_image" alt="Testimonial Image" />
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
        const response = await fetch('https://kabau.pythonanywhere.com/api/testimonials/show/');
        if (!response.ok) {
          throw new Error('Failed to fetch testimonials');
        }
        const data = await response.json();
        if (data && data.length > 0) {
          testimonials.value = data;
          console.log(data);  // Log the data to verify the image URLs
        } else {
          console.error('Error: No data received from API');
        }
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
/* Styles for the testimonial section */
.testimonials {
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
  color: black;
}

.testimonial-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  background: rgba(106, 188, 226, 0.25);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  height: 550px;
  width: 700px;
  color: black;
  position: relative;
  overflow-y: scroll;
  border-radius: 5px;
}

.testimonial-cards::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 10px;
  bottom: 0;
  width: 1px;
  background-color: #000;
  transform: translateX(-50%);
  z-index: 1;
  height: 100vh;
}

.t-cards {
  background: #cacbd5;
  border-radius: 5px;
  padding: 5px;
  margin: 10px;
  width: 250px;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px;
  color: black;
  z-index: 2;
}

.t-cards p {
  margin: 1px;
  color: black;
}

.position {
  font-weight: bold;
}

p {
  margin: 5px 0;
  color: white;
}

span {
  font-style: italic;
  color: #777;
}

.t-image {
  width: 100px;
  height: 100px;
  border-radius: 55px;
  margin-bottom: 10px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .testimonial-cards {
    flex-direction: column; /* Display cards vertically */
    max-height: none; /* Remove maximum height */
    height: auto; /* Set height to auto */
    width: 380px; /* Set width to 100% */
    overflow: hidden;
  }

  .t-cards {
    width: 350px; /* Set card width to 100% for full width */
  }
}

@media (max-width: 430px) {
  .testimonial-cards {
    width: 300px; /* Adjust width for smaller screens */
  }

  .t-cards {
    width: 250px; /* Adjust card width for smaller screens */
  }
}

@media (max-width: 390px) {
  .testimonial-cards {
    width: 250px; /* Adjust width for smaller screens */
  }

  .t-cards {
    width: 200px; /* Adjust card width for smaller screens */
  }
}

@media (max-width: 344px) {
  .testimonial-cards {
    width: 200px; /* Adjust width for smaller screens */
  }

  .t-cards {
    width: 150px; /* Adjust card width for smaller screens */
  }
}

/* Add media queries for other specified screen sizes */
</style>
