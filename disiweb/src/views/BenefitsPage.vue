<template>
  <div v-if="solutions.length > 0" class="outtertext">
    <h3 id="title">Our Services</h3>
    <div class="our-services">
      <ul class="service-list">
        <li v-for="solution in visibleSolutions" :key="solution.id" class="service-item">
          <div class="service-card">
            <img class="service-card-img-top" :src="solution.solution_image" alt="Solution Image">
            <div class="service-card-body">
              <h5 class="service-card-title">{{ solution.name }}</h5>
              <p class="service-card-text">{{ solution.description }}</p>
              <router-link :to="solution.link || '/'" custom v-slot="{ navigate, href }">
                <a @click="navigate" :href="href" class="btn btn-primary">
                  {{ getCTAText(solution.ctatext) }}
                </a>
              </router-link>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const solutions = ref([]);
    const isSmallScreen = ref(window.innerWidth <= 768);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/solutions/show/');
        if (response.data && response.data.length > 0) {
          solutions.value = response.data;
          console.log(response.data);
        } else {
          console.error('Error: No data received from API');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    onMounted(() => {
      fetchData();
      window.addEventListener('resize', () => {
        isSmallScreen.value = window.innerWidth <= 768;
      });
    });

    const getCTAText = (ctatext) => {
      if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/.test(ctatext)) {
        return 'Learn More';
      }
      return ctatext;
    };

    const visibleSolutions = computed(() => {
      return solutions.value;
    });

    return {
      solutions,
      getCTAText,
      visibleSolutions,
      isSmallScreen,
    };
  },
};
</script>


<style scoped>
/* Styles for the solutions section */
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css?family=Varela+Round');

.outtertext{
  text-align: center;
  color: black;
  margin-top: 30px;
}

#title{
  font-size: 40px;
  margin-bottom: -20px;
}

.our-services {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  max-width: 80vw; /* Set maximum width to make it responsive */
  padding: 30px;
  border-radius: 10px;
  margin-bottom: 10px;
  margin-left: 150px;
  flex-wrap: wrap;
}

.service-list {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding-top: 30px;
  margin-right: 20px;
  gap: 20px;
  width: auto; /* Set width to auto for responsive behavior */
}

.service-item {
  flex: 0 0 auto; /* Prevents items from growing or shrinking */
  margin-bottom: 10px;
}

/* Service Card Styles */
.service-card {
  background: #cacbd5;
  border-radius: 10px;
  margin: 5px;
  width: 300px;
  padding: 20px;
  text-align: center;
  color: black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: scale(1.05);
}

.service-card-img-top {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.service-card-body {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  height: 100%;
  align-items: flex-start;
}

.service-card-title {
  font-size: 25px;
}

.service-card-text {
  font-size: 1rem;
  margin-bottom: 1rem;
}

/* Button Styles */
.btn-primary {
  display: flex; /* Enable flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  width: 210px;
  height: 50px;
  border-radius: 10px;
  border: none;
  background: #f2630d;
  color: white;
  text-decoration: none;
}

.btn-primary:hover {
  background: #3a6ea5;
  color: white;
}

/* Responsive adjustments */
@media (max-width: 1000px) {
  .service-card {
    width: 80%; /* Adjust width for smaller screens */
  }

  .service-list {
    flex-wrap: wrap; /* Wrap items for smaller screens */
    justify-content: center; /* Center items on smaller screens */
    overflow: hidden;
  }

  .our-services {
    margin: 20px;
  }
}

@media (max-width: 768px) {
  .service-card {
    width: 90%; /* Further adjust width for smaller screens */
  }

  .service-list {
    flex-direction: column; /* Stack items vertically */
    align-items: center; /* Center items */
    gap: 20px; /* Add some space between items */
  }

  .nav-btn {
    display: none; /* Hide navigation buttons */
  }

  .our-services {
    flex-direction: column; /* Make sure container adapts to column layout */
  }
}
</style>
