<template>
    <div class="our-achievements">
      <h3>Our Services</h3>
      <ul>
         <li v-for="solution in solutions" :key="solution.id"> 
          <CCard style="width: 36rem">
            <CCardImage orientation="top" :src="solution.solution_image" />
            <CCardBody>
              <CCardTitle>{{ solution.name }}</CCardTitle>
              <CCardText>{{ solution.description }}</CCardText>
              <CButton color="primary" href="#">{{ getCTAText(solution.ctatext) }}</CButton>
            </CCardBody>
          </CCard> 
         </li> 

      </ul>
    </div>
  </template>
  
  <script>
  import { reactive, onMounted } from 'vue';
  import axios from 'axios';
  import { CCard, CCardImage, CCardBody, CCardTitle, CCardText, CButton } from '@coreui/vue';
  
  export default {
    components: {
      CCard,
      CCardImage,
      CCardBody,
      CCardTitle,
      CCardText,
      CButton
    },
    setup() {
      const solutions = reactive([]);
  
      const fetchData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/solutions/show/');
          solutions.push(...response.data);
          console.log(response.data);
        } catch (error) {
          console.error('Error fetching data:', error);
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
        solutions,
        getCTAText,
      };
    },
  };
  </script>
  
  <style scoped>
  /* / Styles for the solutions section / */
  </style>
  