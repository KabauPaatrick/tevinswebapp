<template>
    <div class="container mt-5">
        <!-- Testimonials Form -->
        <div class="row">
            <div class="col-md-6 col-md-12">
                <div class="card card-testimonial">
                    <form @submit.prevent="submitTestimonial" class="form">
                        <h2 class="form-title">Create New Testimonial</h2>
                        <div class="form-group">
                            <label for="author" class="form-label">Author:</label>
                            <input type="text" id="author" v-model="testimonial.author" class="form-input" required>
                        </div>
                        <div class="form-group">
                            <label for="position" class="form-label">Position:</label>
                            <input type="text" id="position" v-model="testimonial.position" class="form-input" required>
                        </div>
                        <div class="form-group">
                            <label for="content" class="form-label">Content:</label>
                            <textarea id="content" v-model="testimonial.content" class="form-input" required></textarea>
                        </div>
                        <div class="form-group">
                            <label for="date" class="form-label">Date:</label>
                            <input type="date" id="date" v-model="testimonial.date" class="form-input" required>
                        </div>
                        <div class="form-group">
                            <label for="testimonialImage" class="form-label">Image:</label>
                            <input type="file" id="testimonialImage" @change="handleImageUpload" class="form-input"
                                accept="image/*" required>
                        </div>
                        <div class="form-group">
                            <label for="entity" class="form-label">Entity:</label>
                            <select v-model="testimonial.entity" id="entity" class="form-input" required>
                                <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}
                                </option>
                            </select>
                        </div>
                        <button type="submit" class="btn-submit">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { reactive, onMounted, ref } from 'vue';
import axios from 'axios';

// Define formatDate function outside of the setup function
const formatDate = (dateString) => {
    return new Date(dateString).toISOString().slice(0, 16); // Format the date string
};

export default{
    se









}



</script>