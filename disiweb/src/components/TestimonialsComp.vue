<template>
  <div class="comp-body">
    <div v-if="testimonials.length > 0" class="testimonials">
      <h1>Testimonials</h1>
      <!-- Display cards normally on larger screens -->
      <div v-if="isWideScreen" class="testimonial-cards">
        <div v-for="testimonial in testimonials" :key="testimonial.id" class="t-cards">
          <img class="t-image" :src="testimonial.testimonial_image" alt="Testimonial Image" />
          <p class="author">{{ testimonial.author }}</p>
          <p>{{ testimonial.position }}</p>
          <p>{{ testimonial.content }}</p>
          <div class="rating">
            <span v-for="n in 5" :key="n" :class="{ active: n <= testimonial.rating }">★</span>
          </div>
          <span>- {{ testimonial.author }}, {{ testimonial.position }}</span>
        </div>
      </div>
      <!-- Carousel controls on smaller screens -->
      <div v-else>
        <div class="testimonial-cards">
          <div v-for="(testimonial, index) in testimonials" 
               :key="testimonial.id" 
               v-show="currentCard === index" 
               class="t-cards">
            <img class="t-image" :src="testimonial.testimonial_image" alt="Testimonial Image" />
            <p class="author">{{ testimonial.author }}</p>
            <p>{{ testimonial.position }}</p>
            <p>{{ testimonial.content }}</p>
            <div class="rating">
              <span v-for="n in 5" :key="n" :class="{ active: n <= testimonial.rating }">★</span>
            </div>
            <span>- {{ testimonial.author }}, {{ testimonial.position }}</span>
          </div>
        </div>
        <div class="nav-bar">
          <button class="nav-button prev" @click="prevCard">&lt;</button>
          <div class="dots-container">
            <div v-for="(testimonial, index) in testimonials" 
                 :key="index" 
                 class="dot" 
                 :class="{ active: currentCard === index }" 
                 @click="showCard(index)"></div>
          </div>
          <button class="nav-button next" @click="nextCard">&gt;</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onMounted, onUnmounted } from 'vue';

export default {
  setup() {
    const testimonials = ref([]);
    const currentCard = ref(0);
    const isWideScreen = ref(window.innerWidth > 768);
    let interval;

    const fetchTestimonials = async () => {
      try {
        const response = await fetch('https://kabau.pythonanywhere.com/api/testimonials/show/');
        if (!response.ok) {
          throw new Error('Failed to fetch testimonials');
        }
        const data = await response.json();
        if (data && data.length > 0) {
          testimonials.value = data;
        } else {
          console.error('Error: No data received from API');
        }
      } catch (error) {
        console.error('Error fetching testimonials:', error.message);
      }
    };

    const nextCard = () => {
      currentCard.value = (currentCard.value + 1) % testimonials.value.length;
    };

    const prevCard = () => {
      currentCard.value = (currentCard.value - 1 + testimonials.value.length) % testimonials.value.length;
    };

    const showCard = (index) => {
      currentCard.value = index;
    };

    const handleResize = () => {
      isWideScreen.value = window.innerWidth > 768;
    };

    onMounted(() => {
      fetchTestimonials();
      window.addEventListener('resize', handleResize);

      // Start automatic card switching if on small screens
      if (!isWideScreen.value) {
        interval = setInterval(nextCard, 3000);
      }
    });

    onUnmounted(() => {
      window.removeEventListener('resize', handleResize);
      if (interval) {
        clearInterval(interval);
      }
    });

    return {
      testimonials,
      currentCard,
      isWideScreen,
      nextCard,
      prevCard,
      showCard,
    };
  },
};

</script>

<style scoped>
.comp-body {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #bfbfbd;
  position: relative;
  height: 100vh;
}

.comp-body::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 50%;
  background-image: url('@/assets/images/wave.svg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  z-index: 1;
}

.testimonials {
  position: relative;
  z-index: 2;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: black;
}

.testimonial-cards {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  height: 100%;
  width: 100%;
  position: relative;
}

.t-cards {
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 20px;
  width: 300px;
  height: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px;
  color: black;
  cursor: pointer;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

.t-cards .t-image {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 10px;
  overflow: hidden;
}

.t-cards .author {
  font-weight: bold;
}

.t-cards p {
  margin: 5px 0;
  color: #333;
}

.t-cards span {
  font-style: italic;
  color: #777;
}

.rating {
  display: flex;
  margin: 10px 0;
}

.rating span {
  color: #fbc02d;
  font-size: 18px;
}

.rating span.active {
  color: #fbc02d;
}

/* Nav bar and buttons for carousel */
.nav-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

.nav-bar .dots-container {
  display: flex;
  align-items: center;
}

.nav-bar .dot {
  width: 10px;
  height: 10px;
  margin: 0 5px;
  border-radius: 50%;
  background-color: #ccc;
  cursor: pointer;
  transition: background-color 0.3s;
}

.nav-bar .dot.active {
  background-color: #333;
}

.nav-bar .nav-button {
  background-color: transparent;
  border: none;
  font-size: 24px;
  color: #fff;
  cursor: pointer;
  margin: 0 10px;
  transition: color 0.3s;
}

.nav-bar .nav-button:hover {
  color: #000;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .testimonial-cards {
    flex-direction: column;
    max-height: none;
    height: auto;
    width: 85%;
    overflow: hidden;
  }

  .t-cards {
    width: 100%;
  }
}

@media (max-width: 430px) {
  .testimonial-cards {
    width: 300px;
  }

  .t-cards {
    width: 250px;
  }
}

@media (max-width: 390px) {
  .testimonial-cards {
    width: 250px;
  }

  .t-cards {
    width: 200px;
  }
}

@media (max-width: 344px) {
  .testimonial-cards {
    width: 200px;
  }

  .t-cards {
    width: 150px;
  }
}

</style>
