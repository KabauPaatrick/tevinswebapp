<template>
  <div v-if="isContentAvailable" class="hero">
    <div class="image-container">
      <img :src="content.imageUrl" alt="Hero Image" />
    </div>
    <div class="description">
      <h3>{{ content.title }}</h3>
      <p>{{ content.description }}</p>
      <button class="left-aligned-button" @click="gotoContact">{{ content.ctaText }}</button>
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
        const response = await fetch('http://127.0.0.1:8000/api/homeview/show/');
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
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 40px;
  color: black;
  border-radius: 15px;
  margin-bottom: 30px;
}

.hero h3 {
  font-size: 2rem;
  font-weight: bolder;
  line-height: 1.2;
  margin-bottom: 15px;
  text-align: left;
}

.hero p {
  font-size: 1.5em;
  line-height: 1.5;
  text-align: left;
}

.hero button {
  font-size: 1em;
  background-color: #f2630d;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-top: 20px;
}

.hero button:hover {
  background-color: #3a6ea5;
  color: white;
}

.hero .image-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero img {
  width: 100%;
  max-width: 400px;
  height: auto;
  border-radius: 0px;
}

.hero .description {
  flex: 1;
  padding-left: 20px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .hero h3,  .hero button {
    margin-left: 0;
    margin-right: 0;
    text-align: center;
  }

  .hero p{
    margin-left: 0;
    margin-right: 0;
    text-align: left;
  }

  .hero .description {
    padding-left: 0;
    padding-top: 20px;
  }
}
</style>
