<template>
    <div class="container mt-5">
        <!-- Home View Form -->
        <div class="card mb-4">
            <div class="card-header">
                <h2 class="mb-0">Create New Home View</h2>
            </div>
            <div class="card-body">
                <form @submit.prevent="submitHomeView" class="form">
                    <div class="form-group">
                        <label for="title" class="form-label">Title:</label>
                        <input type="text" id="title" v-model="homeView.title" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="description" class="form-label">Description:</label>
                        <textarea id="description" v-model="homeView.description" class="form-control"
                            required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="ctaText" class="form-label">CTA Text:</label>
                        <input type="text" id="ctaText" v-model="homeView.ctaText" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label for="image" class="form-label">Image:</label>
                        <input type="file" id="image" @change="handleImageUpload" class="form-control" accept="image/*"
                            required>
                    </div>
                    <div class="form-group" v-if="entities.length > 0">
                        <label for="entity" class="form-label">Entity:</label>
                        <select v-model="homeView.entity" id="entity" class="form-control" required>
                            <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}
                            </option>
                        </select>
                    </div>
                    <div v-else>
                        Loading entities...
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-12 d-flex justify-content-between">
                            <button type="submit" class="btn btn-primary">Add Home View</button>
                            <button type="button" class="btn btn-primary"
                                @click="updateHomeView(homeView.id)">Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <!-- Home View Table -->
        <div class="card">
            <div class="card-header">
                <h2 class="mb-0">Home View List</h2>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Title</th>
                                <th>Description</th>
                                <th>CTA Text</th>
                                <th>Image</th>
                                <th>Entity</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(homeView, index) in homeViews" :key="index">
                                <td>{{ homeView.title }}</td>
                                <td>{{ homeView.description }}</td>
                                <td>{{ homeView.ctatext }}</td>
                                <td>
                                    <img :src="homeView.image" alt="Home View Image"
                                        style="max-width: 100px; max-height: 100px;">
                                </td>
                                <td>{{ getEntityName(homeView.entity) }}</td>
                                <td>
                                    <button @click="deleteHomeView(homeView.id)"
                                        class="btn btn-danger mr-2">Delete</button>
                                    <button @click="updateHomeViewForm(homeView)"
                                        class="btn btn-primary">Update</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive, onMounted, ref } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const homeView = reactive({
            id: '',
            title: '',
            description: '',
            ctatext: '',
            image: null,
            entity: '',
        });

        const homeViews = ref([]);
        const entities = ref([]);
        const entitiesFetched = ref(false);

        const fetchEntities = async () => {
            try {
                if (!entitiesFetched.value) {
                    const response = await axios.get('http://127.0.0.1:8000/api/entity/show/');
                    entities.value = response.data;
                    entitiesFetched.value = true;
                }
            } catch (error) {
                console.error('Error fetching entities:', error);
            }
        };

        const fetchHomeViews = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/homeview/show/');
                homeViews.value = response.data;
            } catch (error) {
                console.error('Error fetching home views:', error);
            }
        };

        const submitHomeView = async () => {
            try {
                const formData = new FormData();
                formData.append('title', homeView.title);
                formData.append('description', homeView.description);
                formData.append('ctaText', homeView.ctatext);
                formData.append('image', homeView.image);
                formData.append('entity', homeView.entity);

                const response = await axios.post('http://127.0.0.1:8000/api/homeview/create/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });

                console.log(response.data);

                clearForm();
                fetchHomeViews();
            } catch (error) {
                console.error('Error submitting home view:', error);
            }
        };

        const deleteHomeView = async (id) => {
            try {
                await axios.delete(`http://127.0.0.1:8000/api/homeview/${id}/delete/`);
                fetchHomeViews();
            } catch (error) {
                console.error('Error deleting home view:', error);
            }
        };

        const updateHomeViewForm = (selectedHomeView) => {
            homeView.id = selectedHomeView.id;
            homeView.title = selectedHomeView.title;
            homeView.description = selectedHomeView.description;
            homeView.ctatext = selectedHomeView.ctatext;
            homeView.image = selectedHomeView.image;
            homeView.entity = selectedHomeView.entity;
        };

        const clearForm = () => {
            Object.keys(homeView).forEach(key => {
                homeView[key] = '';
            });
        };

        const handleImageUpload = (event) => {
            homeView.image = event.target.files[0];
        };

        const getEntityName = (entityId) => {
    console.log('Entity ID:', entityId);
    console.log('Entities:', entities.value);
    const entity = entities.value.find(entity => entity.id === entityId);
    console.log('Found Entity:', entity);
    return entity ? entity.name : '';
};


const updateHomeView = async (id) => {
    try {
        const formData = new FormData();
        formData.append('id', homeView.id);
        formData.append('title', homeView.title);
        formData.append('description', homeView.description);
        formData.append('ctaText', homeView.ctatext); // Add ctatext field
        if (homeView.image instanceof File) { // Check if image is a file
            formData.append('image', homeView.image); // Append image file to FormData
        }
        formData.append('entity', homeView.entity);

        const response = await axios.put(`http://127.0.0.1:8000/api/homeview/${id}/update/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        console.log(response.data);

        clearForm();
        fetchHomeViews();
    } catch (error) {
        console.error('Error updating home view:', error);
    }
};


        onMounted(() => {
            fetchEntities();
            fetchHomeViews();
        });

        return {
            homeView,
            homeViews,
            entities,
            submitHomeView,
            deleteHomeView,
            updateHomeViewForm,
            handleImageUpload,
            getEntityName,
            updateHomeView,
        };
    }
};
</script>

<style scoped>
/* Add custom styles here if needed */
.card {
    margin-bottom: 20px;
}
</style>