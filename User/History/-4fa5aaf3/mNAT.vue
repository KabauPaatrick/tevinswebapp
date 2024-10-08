<template>
    <div class="container mt-5">
      <!-- Solution Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Solution</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="submitSolution" class="form">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="name" class="form-label">Name:</label>
                  <input type="text" id="name" v-model="solution.name" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="description" class="form-label">Description:</label>
                  <textarea id="description" v-model="solution.description" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="ctatext" class="form-label">CTA Text:</label>
                  <input type="text" id="ctatext" v-model="solution.ctatext" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="createdBy" class="form-label">Created By:</label>
                  <input type="text" id="createdBy" v-model="solution.createdBy" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="createdAt" class="form-label">Created At:</label>
                  <input type="datetime-local" id="createdAt" v-model="solution.createdAt" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="updatedAt" class="form-label">Updated At</label>
                  <input type="datetime-local" id="updatedAt" v-model="solution.updatedAt" class="form-control" required>
                </div>
              </div>
            </div>
            <div class="form-group">
              <label for="solutionImage" class="form-label">Image:</label>
              <input type="file" id="solution_image" @change="handleImageUpload" class="form-control" accept="image/*" required>
            </div>
            <div class="form-group" v-if="entities.length > 0">
              <label for="entity" class="form-label">Entity:</label>
              <select v-model="solution.entity" id="entity" class="form-control" required>
                <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
  
      <!-- Solution Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Solution List</h2>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                  <th>CTA Text</th>
                  <th>Created By</th>
                  <th>Created At</th>
                  <th>Updated At</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(solution, index) in solutions" :key="index">
                  <td>{{ solution.name }}</td>
                  <td>{{ solution.description }}</td>
                  <td>{{ solution.ctatext }}</td>
                  <td>{{ solution.createdBy }}</td>
                  <td>{{ solution.createdAt }}</td>
                  <td>{{ solution.updatedAt }}</td>
                  <td>
                    <button @click="deleteSolution(solution.id)" class="btn btn-danger">Delete</button>
                    <button @click="updateSolutionForm(solution)" class="btn btn-primary">Update</button>
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
  
      const entities = ref([]);
      const entitiesFetched = ref(false);
  
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
  
      const submitSolution = async () => {
        try {
          const formData = new FormData();
          formData.append('name', solution.name);
          formData.append('description', solution.description);
          formData.append('ctatext', solution.ctatext);
          formData.append('created_by', solution.createdBy); // Use createdBy from solution object
          formData.append('entity', solution.entity);
  
          // Append solution_image only if it's not null
          if (solution.solution_image) {
            formData.append('solution_image', solution.solution_image);
          }
  
          const response = await axios.post('http://127.0.0.1:8000/api/solutions/create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
  
          console.log(response.data);
  
          // Clear the solution fields after successful submission
          Object.keys(solution).forEach(key => {
            solution[key] = '';
          });
  
        } catch (error) {
          console.error('Error submitting solution:', error);
        }
      };
  
      // Function to handle image upload
      const handleImageUpload = (event) => {
        solution.solution_image = event.target.files[0];
        console.log('Image uploaded:', solution.solution_image);
      };
  
      // Fetch entities when component is mounted
      onMounted(() => {
        fetchEntities();
      });
  
      return {
        solution,
        entities,
        submitSolution,
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
  