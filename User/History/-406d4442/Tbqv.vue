<template>
    <div class="our-achievements">
        <h3>Our Achievements</h3>
        <p>Here are some of our notable achievements:</p>
        <ul>
            <li v-for="achievement in achievementsData" :key="achievement.id">
                <div class="achievements">
                    <div class="image-container">
                        <img :src="achievement.achievement_image" alt="">
                    </div>
                    <div class="description">
                        <div class="other-images">
                            <!-- You may add additional logic here to display other images if needed -->
                        </div>
                        <div class="achievement-text">
                            <h3>{{ achievement.name }}</h3>
                            <p>{{ achievement.description }}</p>
                        </div>
                    </div>
                    <div class="background-column">
                       <p></p>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'OurAchievements',
    data() {
        return {
            achievementsData: [],
        };
    },
    async mounted() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/achievement/achievements/');
            this.achievementsData = response.data;
        } catch (error) {
            console.error('Error fetching achievements:', error);
        }
    }
};
</script>

<style>
/* Styles for OurAchievements component */
</style>
