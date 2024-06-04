<template>
  <div v-if="achievements.length > 0" class="achieve">
    <h3>Our Achievements</h3>
    <p id="out">Here are some of our achievements:</p>
    <div class="our-achievement">
      <ul class="achievements-list">
        <li v-for="achievement in achievements" :key="achievement.id" class="achievement-item">
          <div class="a-card">
            <img class="a-card-img-top" :src="achievement.achievement_image" alt="Achievement Image" />
            <div class="a-card-body">
              <h5 class="a-card-title">{{ achievement.name }}</h5>
              <p class="a-card-text">{{ achievement.description }}</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';

export default {
  name: 'OurAchievements',
  setup() {
    const achievements = ref([]);

    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/achievement/show/');
        if (response.data && response.data.length > 0) {
          achievements.value = response.data;
          console.log(achievements.value);
        } else {
          console.error('Error: No data received from API');
        }
      } catch (error) {
        console.error('Error fetching achievements:', error);
      }
    };

    onMounted(fetchData);

    return {
      achievements,
    };
  },
};
</script>

<style scoped>
/* Styles for OurAchievements component */
.achieve {
  text-align: center;
  padding: 20px;
  display: flex;
  flex-direction: column;
  color: white;
}

.our-achievement {
  padding: 20px;
  background: rgba(0, 0, 0, 0.25);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  margin: 30px;
  text-align: center;
  color: black;
}

.our-achievement p {
  color: black;
}

.achievements-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px; /* Space between cards */
  padding: 0;
  margin: 20px 0;
  list-style: none;
}

.achievement-item {
  margin-bottom: 20px;
}

.a-card {
  border: 1px solid #ddd;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 300px;
  padding: 10px;
  background: white;
  display: flex;
  border-radius: 5px;
}

.a-card-img-top {
  width: 120px;
  height: 120px;
}

.a-card-body {
  padding: 20px;
}

.a-card-title {
  font-size: 1.25rem;
  margin-bottom: 0.75rem;
}

.a-card-text {
  margin-bottom: 1.25rem;
}

.btn-primary {
  display: inline-block;
  padding: 0.5rem 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  text-decoration: none;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .a-card {
    width: 100%; /* Adjust card width for smaller screens */
  }

  .a-card-img-top {
    width: 100%;
    height: auto;
  }

  .a-card-body {
    padding: 10px;
  }

  .a-card-title {
    font-size: 1.1rem; /* Decrease title font size for smaller screens */
  }

  .a-card-text {
    font-size: 0.9rem; /* Decrease text font size for smaller screens */
  }
}

@media (max-width: 414px) {
  .achievement-item {
    width: 100%; /* Adjust item width for smaller screens */
  }
}
</style>
