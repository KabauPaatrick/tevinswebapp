<template>
    <div v-if="licenses.length > 0" class="title">
        <h3>License and Registration</h3>
        <div class="liscence">
            <ul class="liscence-list">
                <li v-for="license in licenses" :key="license.id">
                    <div class="liscence-card">
                        <img class="liscence-card-img-top" :src="license.license_images" alt="License Image" />
                        <div class="liscence-card-body">
                            <h5 class="liscence-card-title">{{ license.name }}</h5>
                            <p class="liscence-card-text">{{ license.description }}</p>
                            <a class="btn btn-primary" href="#">{{ getCTAText(license.ctatext) }}</a>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { reactive, onMounted } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const licenses = reactive([]);

        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/license/show/');
                const responseData = response.data;

                if (responseData && responseData.length > 0) {
                    licenses.push(...responseData);
                    console.log(responseData);
                } else {
                    console.error('Error: No data received from API');
                }
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
/* Styles for the title section */
.title {
    text-align: center;
    color: white;
    padding: 20px;
}

.liscence {
    background: rgba(106, 188, 226, 0.25);
    box-shadow: rgb(31 38 135, 0.37);
    backdrop-filter: blur(0px);
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center; /* Center items horizontally */
    overflow-x: auto; /* Add horizontal scroll for small screens */
}

.liscence-list {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 5px;
    gap: 20px;
    overflow: auto; /* Add horizontal scroll for small screens */
    width: auto; /* Set width to auto for responsive behavior */
}

.liscence-card {
    border-radius: 0.25rem;
    margin-bottom: 1rem;
    height: 420px;
    width: 250px;
    padding: 10px;
    background: #0a2472;
}

.liscence-card-img-top {
    width: 100%;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
}

.liscence-card-body {
    padding: 1.25rem;
}

.liscence-card-title {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
}

.liscence-card-text {
    margin-bottom: 1.25rem;
}

.btn {
    display: block;
    background: orangered;
    border: none;
    color: white;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0px;
    box-shadow: rgba(0, 0, 0, 0.9);
    transition: all 200ms ease-in-out;
    text-decoration: none;
}

.btn:hover {
    background: transparent;
    border: solid 1px orangered;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
    .liscence-card {
        width: 85%; /* Adjust width for smaller screens */
        height: 400px; /* Adjust height to fit content */
    }
}

@media (max-width: 768px) {
    .liscence-card {
        width: 80%; /* Adjust width for smaller screens */
        height: auto; /* Adjust height to fit content */
    }

    .liscence-list {
        flex-wrap: wrap; /* Wrap items for smaller screens */
        justify-content: center; /* Center items on smaller screens */
    }

    .liscence {
        margin: 20px;
        padding: 10px;
    }
}

@media (max-width: 430px) {
    .liscence-card {
        width: 90%; /* Adjust width for smaller screens */
    }
}

@media (max-width: 390px) {
    .liscence-card {
        width: 95%; /* Adjust width for smaller screens */
    }
}

@media (max-width: 344px) {
    .liscence-card {
        width: 100%; /* Adjust width for smaller screens */
    }
}

/* Add media queries for other specified screen sizes */
</style>
