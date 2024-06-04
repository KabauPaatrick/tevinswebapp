<template>
    <div v-if="isContentAvailable" class="hero">
      <div class="description">
        <h3>{{ content.title }}</h3>
        <p>{{ content.description }}</p>
        <button class="left-aligned-button" @click="gotoContact">{{ content.ctaText }}</button>
      </div>
      <div class="image-container">
        <img :src="content.imageUrl" alt="Hero Image" />
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
  /* Base styles */
  .hero {
    margin-top: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    background-color: #0a2472;
    padding: 40px;
    height: auto; /* Change height to auto to make it responsive */
    color: white;
    border-radius: 5px;
    margin-bottom: 30px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  }
  
  .hero h3 {
    font-size: 2rem; /* Set a base font size */
    font-weight: bolder;
    line-height: 1.2;
    font-style: normal;
    margin-bottom: 15px;
    text-align: left;
    margin-left: var(--spacing-xl);
    margin-right: var(--spacing-xl);
  }
  
  .hero p {
    font-size: 1.5em;
    line-height: 1.5;
    text-align: left;
    margin-left: var(--spacing-xl);
    margin-right: var(--spacing-xl);
  }
  
  .hero button {
    font-size: 1em;
    background-color: orangered;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    margin-top: 20px;
    text-align: left;
  }
  
  .hero button:hover {
    background-color: transparent;
    color: white;
    border: solid 1px orangered;
  }
  
  .hero .image-container {
    width: 50%; /* Set width to 50% to make it responsive */
    max-width: 50%; /* Ensure image doesn't exceed 50% of the container */
  }
  
  .hero img {
    width: 100%;
    height: auto;
    border-radius: 10px;
  }
  
  .hero .description {
    width: 50%; /* Set width to 50% to make it responsive */
    max-width: 50%; /* Ensure description doesn't exceed 50% of the container */
  }
  
  /* Responsive adjustments */
  @media (max-width: 768px) {
    .hero {
      margin: 20px;
    }
  
    .hero h3 {
      font-size: 1.2rem; /* Decrease font size for smaller screens */
    }
    
    .hero p {
      font-size: 1.2em; /* Decrease font size for smaller screens */
    }
  
    .hero button {
      font-size: 0.8em; /* Decrease font size for smaller screens */
    }
  }
  
  @media (max-width: 1000px) {
    .hero {
      margin: 20px;
    }
  
    .hero button {
      font-size: 0.8em; /* Decrease font size for smaller screens */
    }
  }
  
  /* Specific screen sizes */
  /* IPhone SE */
  @media (max-width: 375px) and (max-height: 667px) {
    .hero h3 {
      font-size: 1rem;
    }
    .hero p {
      font-size: 1em;
    }
    .hero button {
      font-size: 0.8em;
    }
  }
  
  /* IPhone XR */
  @media (max-width: 414px) and (max-height: 896px) {
    .hero h3 {
      font-size: 1.2rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* IPhone 12 Pro */
  @media (max-width: 390px) and (max-height: 884px) {
    .hero h3 {
      font-size: 1.2rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* IPhone 14 Pro Max */
  @media (max-width: 430px) and (max-height: 932px) {
    .hero h3 {
      font-size: 1.2rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* Pixel 7 and Samsung Galaxy S20 Ultra */
  @media (max-width: 412px) and (max-height: 915px) {
    .hero h3 {
      font-size: 1.2rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* Samsung Galaxy S8+ */
  @media (max-width: 360px) and (max-height: 740px) {
    .hero h3 {
      font-size: 1.1rem;
    }
    .hero p {
      font-size: 1.1em;
    }
    .hero button {
      font-size: 0.8em;
    }
  }
  
  /* IPad Mini */
  @media (max-width: 768px) and (max-height: 1024px) {
    .hero h3 {
      font-size: 1.5rem;
    }
    .hero p {
      font-size: 1.4em;
    }
    .hero button {
      font-size: 1em;
    }
  }
  
  /* IPad Air */
  @media (max-width: 820px) and (max-height: 1180px) {
    .hero h3 {
      font-size: 1.7rem;
    }
    .hero p {
      font-size: 1.6em;
    }
    .hero button {
      font-size: 1em;
    }
  }
  
  /* IPad Pro */
  @media (max-width: 1024px) and (max-height: 1366px) {
    .hero h3 {
      font-size: 2rem;
    }
    .hero p {
      font-size: 1.8em;
    }
    .hero button {
      font-size: 1.1em;
    }
  }
  
  /* Surface Pro 7 */
  @media (max-width: 1368px) and (max-height: 312px) {
    .hero h3 {
      font-size: 1.5rem;
    }
    .hero p {
      font-size: 1.4em;
    }
    .hero button {
      font-size: 1em;
    }
  }
  
  /* Surface Duo */
  @media (max-width: 540px) and (max-height: 720px) {
    .hero h3 {
      font-size: 1.3rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* Galaxy Z Fold 5 */
  @media (max-width: 344px) and (max-height: 882px) {
    .hero h3 {
      font-size: 1.1rem;
    }
    .hero p {
      font-size: 1.1em;
    }
    .hero button {
      font-size: 0.8em;
    }
  }
  
  /* Asus Zenbook Fold */
  @media (max-width: 853px) and (max-height: 1280px) {
    .hero h3 {
      font-size: 1.8rem;
    }
    .hero p {
      font-size: 1.7em;
    }
    .hero button {
      font-size: 1em;
    }
  }
  
  /* Samsung Galaxy A51/71 */
  @media (max-width: 412px) and (max-height: 914px) {
    .hero h3 {
      font-size: 1.2rem;
    }
    .hero p {
      font-size: 1.2em;
    }
    .hero button {
      font-size: 0.9em;
    }
  }
  
  /* Nest Hub */
  @media (max-width: 1024px) and (max-height: 600px) {
    .hero h3 {
      font-size: 1.7rem;
    }
    .hero p {
      font-size: 1.6em;
    }
    .hero button {
      font-size: 1em;
    }
  }
  
  /* Nest Hub Max */
  @media (max-width: 1280px) and (max-height: 800px) {
    .hero h3 {
      font-size: 2rem;
    }
    .hero p {
      font-size: 1.8em;
    }
    .hero button {
      font-size: 1.1em;
    }
  }
  
  </style>
  
  