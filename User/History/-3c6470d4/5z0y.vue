<template>

    <div class="admin-panel">
        <!-- Home View Card -->
        <div class="col-md-6 col-md-12">
            <div class="card card-home-view">
                <form @submit.prevent="submitHomeView" class="form">
                    <h2 class="form-title">Create New Home View</h2>
                    <div class="form-group">
                        <label for="title" class="form-label">Title:</label>
                        <input type="text" id="title" v-model="homeView.title" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="description" class="form-label">Description:</label>
                        <textarea id="description" v-model="homeView.description" class="form-input"
                            required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="ctaText" class="form-label">CTA Text:</label>
                        <input type="text" id="ctaText" v-model="homeView.ctatext" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="image" class="form-label">Image:</label>
                        <input type="file" id="image" @change="handleImageUpload" class="form-input" accept="image/*"
                            required>
                    </div>
                    <div class="form-group" v-if="entities.length > 0">
                        <label for="entity" class="form-label">Entity:</label>
                        <select v-model="homeView.entity" id="entity" class="form-input" required>
                            <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}
                            </option>
                        </select>
                    </div>
                    <div v-else>
                        Loading entities...
                    </div>
                    <button type="submit" class="btn-submit">Submit</button>
                </form>
            </div>
        </div>

        <!-- Achievement Card -->
        <div class="col-md-6 col-md-12">
            <div class="card card-achievement">
                <form @submit.prevent="submitAchievement" class="form">
                    <h2 class="form-title">Create New Achievement</h2>
                    <div class="form-group">
                        <label for="name" class="form-label">Name:</label>
                        <input type="text" id="name" v-model="achievement.name" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="description" class="form-label">Description:</label>
                        <textarea id="description" v-model="achievement.description" class="form-input"
                            required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="startYear" class="form-label">Start Year:</label>
                        <input type="number" id="startYear" v-model="achievement.startYear" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="endYear" class="form-label">End Year:</label>
                        <input type="number" id="endYear" v-model="achievement.endYear" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="achievementDate" class="form-label">Achievement Date:</label>
                        <input type="date" id="achievementDate" v-model="achievement.achievementDate" class="form-input"
                            required>
                    </div>
                    <div class="form-group">
                        <label for="isCompleted" class="form-label">Is Completed:</label>
                        <input type="checkbox" id="isCompleted" v-model="achievement.isCQompleted">
                    </div>
                    <div class="form-group">
                        <label for="rating" class="form-label">Rating:</label>
                        <input type="number" id="rating" v-model="achievement.rating" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="image" class="form-label">Image:</label>
                        <input type="file" id="image" @change="handleImageUpload" class="form-input" accept="image/*"
                            required>
                    </div>

                    <div class="form-group">
                        <label for="createdBy" class="form-label">Created By:</label>
                        <input type="text" id="createdBy" v-model="achievement.createdBy" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="createdAt" class="form-label">Created At:</label>
                        <input type="datetime-local" id="createdAt" v-model="achievement.createdAt" class="form-input"
                            required>
                    </div>
                    <div class="form-group">
                        <label for="updatedAt" class="form-label">Updated At</label>
                        <input type="datetime-local" id="updatedAt" v-model="achievement.updatedAt" class="form-input"
                            required>
                    </div>
                    <div class="form-group" v-if="entities.length > 0">
                        <label for="entity" class="form-label">Entity:</label>
                        <select v-model="achievement.entity" id="entity" class="form-input" required>
                            <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}
                            </option>
                        </select>
                    </div>
                    <div class="form-group" v-if="customers.length > 0">
                        <label for="customer" class="form-label">Customer:</label>
                        <select v-model="achievement.customer" id="customer" class="form-input" required>
                            <option v-for="customer in customers" :key="customer.id" :value="customer.id">{{ customer.id
                                }}</option>
                        </select>
                    </div>


                    <button type="submit" class="btn-submit" @click="submitAchievement">Submit</button>
                </form>
            </div>
        </div>
        <div class="col-md-6 col-md-12">
            <div class="card card-home-view">
                <form @submit.prevent="submitSolution" class="form">
                    <h2 class="form-title">Create New Solution</h2>
                    <div class="form-group">
                        <label for="name" class="form-label">Name:</label>
                        <input type="text" id="name" v-model="solution.name" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="description" class="form-label">Description:</label>
                        <textarea id="description" v-model="solution.description" class="form-input"
                            required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="ctatext" class="form-label">CTA Text:</label>
                        <input type="text" id="ctatext" v-model="solution.ctatext" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="createdBy" class="form-label">Created By:</label>
                        <input type="text" id="createdBy" v-model="solution.createdBy" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="createdAt" class="form-label">Created At:</label>
                        <input type="datetime-local" id="createdAt" v-model="solution.createdAt" class="form-input"
                            required>
                    </div>
                    <div class="form-group">
                        <label for="updatedAt" class="form-label">Updated At</label>
                        <input type="datetime-local" id="updatedAt" v-model="solution.updatedAt" class="form-input"
                            required>
                    </div>
                    <div class="form-group">
                        <label for="solutionImage" class="form-label">Image:</label>
                        <input type="file" id="solution_image" @change="handleImageUpload" class="form-input"
                            accept="image/*" required>
                    </div>
                    <div class="form-group" v-if="entities.length > 0">
                        <label for="entity" class="form-label">Entity:</label>
                        <select v-model="solution.entity" id="entity" class="form-input" required>
                            <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}
                            </option>
                        </select>
                    </div>
                    <button type="submit" class="btn-submit" @click="submitSolution">Submit</button>
                </form>
            </div>
        </div>
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
        <div class="col-md-6 col-md-12">
            <div class="card card-entity">
                <form @submit.prevent="submitEntity" class="form">
                    <h2 class="form-title">Create New Entity</h2>
                    <div class="form-group">
                        <label for="name" class="form-label">Name:</label>
                        <input type="text" id="name" v-model="entity.name" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="description" class="form-label">Description:</label>
                        <textarea id="description" v-model="entity.description" class="form-input" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="location" class="form-label">Location:</label>
                        <input type="text" id="location" v-model="entity.location" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="contactPerson" class="form-label">Contact Person:</label>
                        <input type="text" id="contactPerson" v-model="entity.contact_person" class="form-input"
                            required>
                    </div>
                    <div class="form-group">
                        <label for="email" class="form-label">Email:</label>
                        <input type="email" id="email" v-model="entity.email" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label for="phoneNumber" class="form-label">Phone Number:</label>
                        <input type="tel" id="phoneNumber" v-model="entity.phone_number" class="form-input" required>
                    </div>
                    <button type="submit" class="btn-submit" @click="submitEntity">Submit</button>
                </form>
            </div>
        </div>
        <div class="customer-form">
            <form @submit.prevent="submitCustomer" class="form">
                <h2 class="form-title">Create New Customer</h2>
                <div class="form-group">
                    <label for="name" class="form-label">Name:</label>
                    <input type="text" id="name" v-model="customer.name" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="email" class="form-label">Email:</label>
                    <input type="email" id="email" v-model="customer.email" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="phone_number" class="form-label">Phone Number:</label>
                    <input type="tel" id="phone_number" v-model="customer.phone_number" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="address" class="form-label">Address:</label>
                    <input type="text" id="address" v-model="customer.address" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="city" class="form-label">City:</label>
                    <input type="text" id="city" v-model="customer.city" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="state" class="form-label">State:</label>
                    <input type="text" id="state" v-model="customer.state" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="country" class="form-label">Country:</label>
                    <input type="text" id="country" v-model="customer.country" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="postal_code" class="form-label">Postal Code:</label>
                    <input type="text" id="postal_code" v-model="customer.postal_code" class="form-input" required>
                </div>
                <div class="form-group">
                    <label for="created_by" class="form-label">Created By:</label>
                    <input type="text" id="created_by" v-model="customer.created_by" class="form-input" required>
                </div>
                <button type="submit" class="btn-submit" @click="submitCustomer">Submit</button>
            </form>
        </div>
    </div>
</template>
<script>
import { reactive, onMounted, ref } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const homeView = reactive({
            title: '',
            description: '',
            ctatext: '',
            image: null,
            entity: '',
        });

        const achievement = reactive({
            name: '',
            description: '',
            startYear: '',
            endYear: '',
            achievementDate: '',
            isCompleted: true,
            rating: 1,
            achievement_image: null,
            createdBy: '',
            createdAt: '',
            updatedAt: '',
            entity: '',
            customer: '',
        });
        const customer = reactive({
            name: '',
            email: '',
            phone_number: '',
            address: '',
            city: '',
            state: '',
            country: '',
            postal_code: '',
            created_by: ''
        });

        const solution = reactive({
            name: '',
            description: '',
            ctatext: '',
            solution_image: null,
            createdBy: '',
            createdAt: '',
            updatedAt: '',
            entity: '',
        });
        const testimonial = reactive({
            author: '',
            position: '',
            content: '',
            date: '',
            testimonialImage: null,
            entity: '',
        });
        const entity = reactive({
            name: '',
            description: '',
            location: '',
            contact_person: '',
            email: '',
            phone_number: '',
        });


        const entities = ref([]);
        const entitiesFetched = ref(false);

        const customers = ref([]);
        const customersFetched = ref(false);

        const fetchEntities = async () => {
            try {
                if (!entitiesFetched.value) {
                    const response = await axios.get('http://127.0.0.1:8000/api/entity/entities/');
                    entities.value = response.data;
                    entitiesFetched.value = true;
                }
            } catch (error) {
                console.error('Error fetching entities:', error);
            }
        };

        const fetchCustomers = async () => {
            try {
                if (!customersFetched.value) {
                    const response = await axios.get('http://127.0.0.1:8000/api/customer/customers/');
                    customers.value = response.data;
                    customersFetched.value = true;
                }
            } catch (error) {
                console.error('Error fetching customers:', error);
            }
        };
        const submitTestimonial = async () => {
            try {
                const formData = new FormData();
                formData.append('author', testimonial.author);
                formData.append('position', testimonial.position);
                formData.append('content', testimonial.content);
                formData.append('date', testimonial.date);
                formData.append('testimonial_image', testimonial.testimonialImage);
                formData.append('entity', testimonial.entity);

                const response = await axios.post('http://127.0.0.1:8000/api/testimonials/create/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                console.log(response.data);

                // Clear form fields after successful submission
                Object.keys(testimonial).forEach(key => {
                    testimonial[key] = '';
                });

            } catch (error) {
                console.error('Error submitting testimonial:', error);
            }
        };


        const submitHomeView = async () => {
            try {
                const formData = new FormData();
                formData.append('title', homeView.title);
                formData.append('description', homeView.description);
                formData.append('ctatext', homeView.ctatext);
                formData.append('image', homeView.image);
                formData.append('entity', homeView.entity);

                const response = await axios.post('http://127.0.0.1:8000/api/homeview/homeviews/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                console.log(response.data);

                Object.keys(homeView).forEach(key => {
                    homeView[key] = '';
                });

            } catch (error) {
                console.error('Error submitting home view:', error);
            }
        };

        const submitAchievement = async () => {
            try {
                const formData = new FormData();
                formData.append('name', achievement.name);
                formData.append('description', achievement.description);
                formData.append('start_year', achievement.startYear);
                formData.append('end_year', achievement.endYear);
                formData.append('achievement_date', achievement.achievementDate);
                formData.append('is_completed', achievement.isCompleted);
                formData.append('rating', achievement.rating);
                formData.append('created_by', achievement.createdBy);
                formData.append('created_at', achievement.createdAt);
                formData.append('updated_at', achievement.updatedAt);
                formData.append('entity', achievement.entity);
                formData.append('customer', achievement.customer);
                formData.append('achievement_image', achievement.achievement_image);

                const response = await axios.post('http://127.0.0.1:8000/api/achievement/achievements/', formData);

                console.log(response.data);

                Object.keys(achievement).forEach(key => {
                    achievement[key] = '';
                });

            } catch (error) {
                console.error('Error submitting achievement:', error);
            }
        };

        const submitSolution = async () => {
            try {
                const formData = new FormData();
                formData.append('name', solution.name);
                formData.append('description', solution.description);
                formData.append('ctatext', solution.ctatext);
                formData.append('created_by', solution.createdBy); // Use createdBy from solution object
                formData.append('created_at', solution.createdAt);
                formData.append('updated_at', solution.updatedAt);
                formData.append('solution_image', solution.solution_image);
                formData.append('entity', solution.entity);

                const response = await axios.post('http://127.0.0.1:8000/api/solutions/create/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                console.log(response.data);

                Object.keys(solution).forEach(key => {
                    solution[key] = '';
                });

            } catch (error) {
                console.error('Error submitting solution:', error);
            }
        };
        const submitEntity = async () => {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/entity/entities/', entity);

                console.log(response.data);

                // Clear form fields after successful submission
                Object.keys(entity).forEach(key => {
                    entity[key] = '';
                });

            } catch (error) {
                console.error('Error submitting entity:', error);
            }
        };

        const handleImageUpload = (event) => {
            const file = event.target.files[0];
            homeView.image = file;
            achievement.achievement_image = file;
            solution.solution_image = file;
            testimonial.testimonialImage = file;
        };
        const submitCustomer = async () => {
            try {
                const formData = new FormData();
                formData.append('name', customer.name);
                formData.append('email', customer.email);
                formData.append('phone_number', customer.phone_number);
                formData.append('address', customer.address);
                formData.append('city', customer.city);
                formData.append('state', customer.state);
                formData.append('country', customer.country);
                formData.append('postal_code', customer.postal_code);
                formData.append('created_by', customer.created_by);

                const response = await axios.post('http://127.0.0.1:8000/api/customer/customers/', formData);
                console.log(response.data);

                // Clear form fields after successful submission
                Object.keys(customer).forEach(key => {
                    customer[key] = '';
                });
            } catch (error) {
                console.error('Error submitting customer:', error);
            }

          
        }

            return { entity, testimonial, homeView, achievement, solution, entities, customers, submitHomeView, submitAchievement, submitSolution, handleImageUpload, submitTestimonial, submitEntity, customer, submitCustomer };

            onMounted(() => {
                fetchEntities();
                fetchCustomers();
            });

    }
}
</script>

<style scoped>
.admin-panel {
    margin: 20px;
    display: flex;
    flex-wrap: wrap;
}

.card {
    flex: 1 1 calc(50% - 20px);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    margin-right: 20px;
}

.card-entity {
    background-color: #f7f7f7;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.card-testimonial {
    background-color: #f7f7f7;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}


.card-home-view {
    background-color: #f7f7f7;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.card-achievement {
    background-color: #fafafa;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form {
    background-color: inherit;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 24px;
    color: #333;
}

.form-group {
    margin-bottom: 20px;
}

.form-label {
    font-weight: bold;
    color: #555;
}

.form-input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.form-input:focus {
    outline: none;
    border-color: #007bff;
}

.btn-submit {
    display: block;
    width: 100%;
    padding: 12px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.3s ease;
}

.btn-submit:hover {
    background-color: #0056b3;
}

/* Optional: Add hover effects to form inputs */
.form-input:hover {
    border-color: #999;
}

/* Optional: Add margin between form inputs */
.form-input:not(:last-child) {
    margin-bottom: 10px;
}

/* Styles for the admin panel */
</style>