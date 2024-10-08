<template>
    <div class="container mt-5">
      <!-- Achievement Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Achievement</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="submitAchievement" class="form">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="name" class="form-label">Name:</label>
                  <input type="text" id="name" v-model="achievement.name" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="description" class="form-label">Description:</label>
                  <textarea id="description" v-model="achievement.description" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="startYear" class="form-label">Start Year:</label>
                  <input type="number" id="startYear" v-model="achievement.start_year" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="endYear" class="form-label">End Year:</label>
                  <input type="number" id="endYear" v-model="achievement.end_year" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="achievementDate" class="form-label">Achievement Date:</label>
                  <input type="date" id="achievementDate" v-model="achievement.achievement_date" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="isCompleted" class="form-label">Is Completed:</label>
                  <input type="checkbox" id="isCompleted" v-model="achievement.is_completed">
                </div>
                <div class="form-group">
                  <label for="rating" class="form-label">Rating:</label>
                  <input type="number" id="rating" v-model="achievement.rating" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="achievementImage" class="form-label">Achievement Image:</label>
                  <input type="file" id="achievementImage" @change="handleImageUpload" class="form-control" accept="image/*" required>
                </div>
                <div class="form-group">
                  <label for="createdBy" class="form-label">Created By:</label>
                  <input type="text" id="createdBy" v-model="achievement.created_by" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="createdAt" class="form-label">Created At:</label>
                  <input type="datetime-local" id="createdAt" v-model="achievement.created_at" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="updatedAt" class="form-label">Updated At:</label>
                  <input type="datetime-local" id="updatedAt" v-model="achievement.updated_at" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="entity" class="form-label">Entity:</label>
                  <input type="text" id="entity" v-model="achievement.entity" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="customer" class="form-label">Customer:</label>
                  <input type="text" id="customer" v-model="achievement.customer" class="form-control" required>
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Add Achievement</button>
                <button type="button" class="btn btn-primary" @click="updateAchievementForm(achievement)">Update</button>
              </div>
            </div>
          </form>
        </div>
      </div>
  
      <!-- Achievement Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Achievement List</h2>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Start Year</th>
                  <th>End Year</th>
                  <th>Achievement Date</th>
                  <th>Is Completed</th>
                  <th>Rating</th>
                  <th>Achievement Image</th>
                  <th>Created By</th>
                  <th>Created At</th>
                  <th>Updated At</th>
                  <th>Entity</th>
                  <th>Customer</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(achievement, index) in achievements" :key="index">
                  <td>{{ achievement.name }}</td>
                  <td>{{ achievement.description }}</td>
                  <td>{{ achievement.start_year }}</td>
                  <td>{{ achievement.end_year }}</td>
                  <td>{{ achievement.achievement_date }}</td>
                  <td>{{ achievement.is_completed }}</td>
                  <td>{{ achievement.rating }}</td>
                  <td>{{ achievement.achievement_image }}</td>
                  <td>{{ achievement.created_by }}</td>
                  <td>{{ achievement.created_at }}</td>
                  <td>{{ achievement.updated_at }}</td>
                  <td>{{ achievement.entity }}</td>
                  <td>{{ achievement.customer }}</td>
                  <td class="d-flex">
                    <button @click="deleteAchievement(achievement.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateAchievementForm(achievement)" class="btn btn-primary">Update</button>
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
      const achievement = reactive({
        id:'',
        name: '',
        description: '',
        start_year: '',
        end_year: '',
        achievement_date: '',
        is_completed: true,
        rating: 1,
        achievement_image: null,
        created_by: '',
        created_at: '',
        updated_at: '',
        entity: '',
        customer: '',
      });
  
      const achievements = ref([]);
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
  
      const fetchAchievements = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/achievement/show');
          achievements.value = response.data;
        } catch (error) {
          console.error('Error fetching achievements:', error);
        }
      };
  
      const submitAchievement = async () => {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/achievement/achievements/', achievement);
          console.log(response.data);
          clearForm();
          fetchAchievements();
        } catch (error) {
          console.error('Error submitting achievement:', error);
        }
      };
  
      const deleteAchievement = async (id) => {
        try {
          await axios.delete(`http://127.0.0.1:8000/api/achievement/${id}/delete`);
          fetchAchievements();
        } catch (error) {
          console.error('Error deleting achievement:', error);
        }
      };
  
      const updateAchievementForm = (selectedAchievement) => {
        achievement.name = selectedAchievement.name;
        achievement.description = selectedAchievement.description;
        achievement.start_year = selectedAchievement.start_year;
        achievement.end_year = selectedAchievement.end_year;
        achievement.is_completed = selectedAchievement.is_completed;
        achievement.rating = selectedAchievement.rating;
        achievement.achievement_image = selectedAchievement.achievement_image;
        achievement.achievement_date = selectedAchievement.achievement_date;
        achievement.created_by = selectedAchievement.created_by;
        achievement.created_at = selectedAchievement.created_at;
        achievement.updated_at = selectedAchievement.updated_at;
        achievement.entity = selectedAchievement.entity;
        achievement.customer = selectedAchievement.customer;
      };
  
      const clearForm = () => {
        Object.keys(achievement).forEach(key => {
          achievement[key] = '';
        });
      };
  
      const handleImageUpload = (event) => {
        achievement.achievement_image = event.target.files[0];
      };
  
      onMounted(() => {
        fetchAchievements();
      });
  
      return {
        achievement,
        achievements,
        submitAchievement,
        deleteAchievement,
        updateAchievementForm,
        handleImageUpload
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
  