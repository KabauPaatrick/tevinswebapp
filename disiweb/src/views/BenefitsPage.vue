<template>
  <div v-if="solutions.length > 0" class="outtertext">
    <h3>Our Services</h3>
    <div class="our-services">
      <button v-if="!isSmallScreen && solutions.length > 3" @click="prev" class="nav-btn left-btn">&lt;</button>
      <ul class="service-list">
        <li v-for="solution in visibleSolutions" :key="solution.id" class="service-item">
          <div class="service-card">
            <img class="service-card-img-top" :src="solution.solution_image" alt="Solution Image">
            <div class="service-card-body">
              <h5 class="service-card-title">{{ solution.name }}</h5>
              <p class="service-card-text">{{ solution.description }}</p>
              <a :href="solution.link || '#'" class="btn btn-primary">{{ getCTAText(solution.ctatext) }}</a>
            </div>
          </div>
        </li>
      </ul>
      <button v-if="!isSmallScreen && solutions.length > 3" @click="next" class="nav-btn right-btn">&gt;</button>
    </div>
  </div>
</template>

<script>
import { reactive, ref, onMounted, computed } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const solutions = reactive([]);
    const currentIndex = ref(0);
    const isSmallScreen = ref(window.innerWidth <= 768);

    const fetchData = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/solutions/show/');
        if (response.data && response.data.length > 0) {
          solutions.push(...response.data);
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
      if (isSmallScreen.value) {
        return solutions;
      }
      return solutions.slice(currentIndex.value, currentIndex.value + 3);
    });

    const next = () => {
      if (currentIndex.value + 3 < solutions.length) {
        currentIndex.value += 3;
      }
    };

    const prev = () => {
      if (currentIndex.value > 0) {
        currentIndex.value -= 3;
      }
    };

    return {
      solutions,
      getCTAText,
      visibleSolutions,
      next,
      prev,
      isSmallScreen,
    };
  },
};
</script>

<style scoped>
/* Styles for the solutions section */
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css?family=Varela+Round');

/* Color Variables */
:root {
  --color-one: #1F2124;
  --color-two: #383A3F;
  --color-three: #F68657;
  --color-four: #F6B352;
}

*, *::before, *::after {
  box-sizing: border-box;
}

body {
  background: var(--color-two);
  font-family: 'Varela Round', sans-serif;
}

.outtertext {
  text-align: center;
  color: black;
  margin-top: 30px;
}

.our-services {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  max-width: 100%; /* Set maximum width to make it responsive */
  padding: 30px;
  border-radius: 10px;
  margin-bottom: 10px;
  background: rgba(106, 188, 226, 0.25);
  box-shadow: rgb(31 38 135, 0.37);
  backdrop-filter: blur(0px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  overflow-x: auto; /* Add horizontal scroll for small screens */
}

.our-services h3 {
  color: white;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.service-list {
  display: flex;
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
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
  border-radius: 5px;
  margin: 20px;
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
  justify-content: space-between;
  height: 100%;
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
  display: block;
  background: orangered;
  border: none;
  color: white;
  padding: 15px 20px;
  margin: 20px 0;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.9);
  transition: all 200ms ease-in-out;
  text-decoration: none;
}

.btn-primary:hover {
  background: #3a6ea5;
}

/* Navigation Button Styles */
.nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px 20px;
  width: 30px;
  height: 70px;
  cursor: pointer;
  z-index: 1;
}

.left-btn {
  left: 10px;
}

.right-btn {
  right: 10px;
}

/* Specific styles for the middle card */
.service-item:nth-child(2) .service-card {
  transform: scale(1.1) translateY(-10px);
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.5);
}

.service-item:nth-child(2) .service-card:hover {
  transform: scale(1.15);
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
