<template>
  <div v-if="isContentAvailable" class="hero" :style="{ backgroundImage: `url(${content.imageUrl})` }">
    <div class="overlay"></div>
    <div class="hero-description">
      <h3>{{ content.title }}</h3>
      <p>{{ content.description }}</p>
      <button class="hero-button" @click="gotoContact">{{ content.ctaText }}</button>
    </div>
  </div>
</template>

<script>
import router from '@/router';
import { reactive, onMounted, computed } from 'vue';

export default {
  setup() {
    const content = reactive({
      title: "",
      description: "",
      ctaText: "",
      imageUrl: '',
    });

    // Fetch data from the Django API when the component is mounted
    onMounted(async () => {
      try {
        const response = await fetch('https://kabau.pythonanywhere.com/apis/homeview/show/');
        const responseData = await response.json();

        if (responseData && responseData.length > 0) {
          const data = responseData[0]; // Assuming you only want the first item
          if (data.title && data.description && data.image) {
            content.title = data.title;
            content.description = data.description;
            content.ctaText = data.ctaText || "Contact Us"; // Fallback to "Contact Us" if ctaText is empty
            content.imageUrl = data.image;
            console.log("Data from API:", data);
          } else {
            console.error('Error: Missing required data fields');
          }
        } else {
          console.error('Error: No data received from API');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    });

    const isContentAvailable = computed(() => {
      return content.title && content.description && content.imageUrl;
    });

    const gotoContact = () => {
      router.push('/contact');
    };

    return {
      content,
      gotoContact,
      isContentAvailable,
    };
  }
};
</script>

<style scoped>
.hero {
  position: relative; /* Ensure relative positioning for stacking */
  display: flex;
  align-items: center; /* Center vertically */
  justify-content: center; /* Center horizontally */
  flex-direction: column;
  padding: 40px;
  margin-bottom: 30px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 70vh;
  text-align: center;
  color: white; /* Adjust text color for better contrast */
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent overlay */
}

.hero-description {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center; /* Center horizontally */
  justify-content: center; /* Center vertically */
  max-width: 80%;
  
}

.hero h3 {
  font-size: 50px;
  line-height: 1.2;
  margin-bottom: 15px;
}

.hero p {
  font-size: 25px;
  line-height: 1.5;
  margin-bottom: 15px;
}

.hero-button {
  font-size: 1em;
  background-color: #f2630d;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

.hero button:hover {
  background-color: #3a6ea5;
}

@media screen and (max-width: 768px) {
  .hero {
    height: 100vh; /* Adjust height for smaller screens */
  }

  .hero h3 {
    font-size: 6vw; /* Adjust font size for smaller screens */
  }

  .hero p {
    font-size: 4vw; /* Adjust font size for smaller screens */
  }

  .cta-button {
    font-size: 3vw; /* Adjust font size for smaller screens */
  }
}
</style>

