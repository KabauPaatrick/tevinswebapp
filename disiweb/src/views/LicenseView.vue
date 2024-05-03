<template>
    <div class="our-achievements">
        <!-- <h3>License and Registration</h3> -->
        <ul>
            <li v-for="license in licenses" :key="license.id">
          <CCard style="width: 36rem">
            <CCardImage orientation="top" :src="license.license_images" />
            <CCardBody>
              <CCardTitle>{{ license.name }}</CCardTitle>
              <CCardText>{{ license.description }}</CCardText>
              <CButton color="primary" href="#">{{ getCTAText(license.ctatext) }}</CButton>
            </CCardBody>
          </CCard>
         </li>
        </ul>
                
       
        <!-- <h2>License and Registration</h2>
            
        <ul>
            <li v-for="license in licenses" :key="license.id">
                <div class="description">
                    <div class="card">
                        <h3>{{ license.name }}</h3>
                        <p>{{ license.description }}</p>
                        <button class="left-aligned-button">{{ getCTAText(license.ctatext) }}</button>
                    </div>
                </div>
                <div class="image-container">
                    <img :src="license.license_images" alt="Hero Image" />
                </div>
            </li>
        </ul> -->
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
        const licenses = reactive([]);

        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/license/show/');
                const responseData = response.data;

                licenses.push(...responseData);
                console.log(responseData);
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
            licenses,
            getCTAText

        };
    },
};
</script>

<style scoped>
/* //.benefits {}
    /* Styles for the benefits section */
</style>
