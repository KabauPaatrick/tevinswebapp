<template>
    <div class="our-achievements">
      <!-- <h3>Our Achievements</h3>
      <p>Here are some of our achievements:</p> -->
      <ul>
        <li v-for="achievement in achievements" :key="achievement.id">
          <CCard style="width: 36rem">
            <CCardImage orientation="top" :src="achievement.achievement_image" />
            <CCardBody>
              <CCardTitle>{{ achievement.name }}</CCardTitle>
              <CCardText>{{ achievement.description }}</CCardText>
              <!-- <CButton color="primary" href="#">{{ getCTAText(achievement.ctatext) }}</CButton> -->
            </CCardBody>
          </CCard>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import axios from 'axios';
  import { CCard, CCardImage, CCardBody, CCardTitle, CCardText} from '@coreui/vue';
  
  export default {
    name: 'OurAchievements',
    components: {
      CCard,
      CCardImage,
      CCardBody,
      CCardTitle,
      CCardText,
    //   CButton
    },
    setup() {
      const achievements = ref([]);
  
      const fetchData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/achievement/show/');
          achievements.value = response.data;
          console.log(achievements.value)
        } catch (error) {
          console.error('Error fetching achievements:', error);
        }
      };
  
      onMounted(fetchData);
  
      const getCTAText = (ctatext) => {
        // Check if ctatext is in timestamp format
        if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/.test(ctatext)) {
          return "Learn More";
        }
        return ctatext; // Return ctatext as is
      };
  
      return {
        achievements,
        getCTAText
      };
    }
  };
  </script>
  
  <style>
  /* Styles for OurAchievements component */
  </style>
  