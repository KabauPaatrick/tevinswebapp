<template>
    <div class="hero">
        <div class="description">
            <h3>{{ content.title }}</h3>
            <p>{{ content.description }}</p>
            <button class="left-aligned-button">{{ content.ctaText }}</button>
        </div>
        <div class="image-container">
            <img :src="content.imageUrl" alt="Hero Image" />
        </div>
    </div>
</template>

<script>
import { reactive, onMounted } from 'vue';

export default {
    setup() {
        const content = reactive({
            title: "",
            description: "",
            ctaText: "",
            imageUrl: '',
        })

        // Fetch data from the Django API when the component is mounted
        onMounted(async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/api/homeview/show/');
                const responseData = await response.json();
                
                if (responseData && responseData.length > 0) {
                    const data = responseData[0]; // Assuming you only want the first item
                    content.title = data.title;
                    content.description = data.description;
                    content.ctaText = data.ctaText || "Learn More"; // Fallback to "Learn More" if ctaText is empty
                    content.imageUrl = data.image;
                    console.log("Data from API:", data);
                } else {
                    console.error('Error: No data received from API');
                }
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        });

        return {
            content,
        };
    }
};
</script>

<style scoped>
.hero {
  
}
</style>
