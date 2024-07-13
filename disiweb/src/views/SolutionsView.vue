<template>
  <div>
    <AdminNav />
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
                <!-- Input fields for solution -->
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
                <div class="form-group">
                  <label for="createdBy" class="form-label">Created By:</label>
                  <input type="text" id="createdBy" v-model="solution.created_by" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="createdAt" class="form-label">Created At:</label>
                  <input type="datetime-local" id="createdAt" v-model="solution.createdAt" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="updatedAt" class="form-label">Updated At:</label>
                  <input type="datetime-local" id="updatedAt" v-model="solution.updatedAt" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <!-- Input fields for solution -->
                <div class="form-group">
                  <label for="solutionImage" class="form-label">Image:</label>
                  <input type="file" id="solutionImage" @change="handleImageUpload" class="form-control" accept="image/*" required>
                </div>
                <!-- Entity field -->
                <div class="form-group">
                  <label for="entity" class="form-label">Entity:</label>
                  <select v-model="solution.entity" id="entity" class="form-control" required>
                    <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}</option>
                  </select>
                </div>
              </div>
            </div>
            <!-- Submit and update buttons -->
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Add Solution</button>
                <button type="button" class="btn btn-primary" @click="updateSolutiononSubmit(solution.id)">Update Solution</button>
              </div>
            </div>
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
                  <th>Image</th>
                  <th>Created By</th>
                  <th>Created At</th>
                  <th>Updated At</th>
                  <th>Entity</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(solution, index) in solutions" :key="index">
                  <td>{{ solution.name }}</td>
                  <td>{{ solution.description }}</td>
                  <td>{{ solution.ctatext }}</td>
                  <td><img :src="solution.solution_image" alt="Solution Image" style="max-width: 100px;"></td>
                  <td>{{ solution.created_by }}</td>
                  <td>{{ solution.createdAt }}</td>
                  <td>{{ solution.updatedAt }}</td>
                  <td>{{ getEntityName(solution.entity) }}</td>
                  <td class="d-flex">
                    <button @click="deleteSolution(solution.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateSolutionForm(solution)" class="btn btn-primary">Update</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { reactive, onMounted, ref } from 'vue';
  import axios from 'axios';
  import AdminNav from '@/components/AdminNav.vue';
  
  export default {
    name: 'NewAdminNPage', 
    components: {
      AdminNav,
    },
    setup() {
      const solution = reactive({
        id:'',
        name: '',
        description: '',
        ctatext: '',
        solution_image: null,
        created_by: '',
        createdAt: null,
        updatedAt: null,
        entity: '',
      });
  
      const entities = ref([]);
      const solutions = ref([]);
  
      const fetchEntities = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/entity/show/');
          entities.value = response.data;
        } catch (error) {
          console.error('Error fetching entities:', error);
        }
      };
  
      const fetchSolutions = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/solutions/show/');
          solutions.value = response.data.map(solution => ({
            ...solution,
            createdAt: formatDate(solution.createdAt),
            updatedAt: formatDate(solution.updatedAt)
          }));
        } catch (error) {
          console.error('Error fetching solutions:', error);
        }
      };
  
      const submitSolution = async () => {
        try {
          const formData = new FormData();
          formData.append('id',solution.id);
          formData.append('name', solution.name);
          formData.append('description', solution.description);
          formData.append('ctatext', solution.ctatext);
          formData.append('created_by', solution.created_by);
          formData.append('entity', solution.entity);
          formData.append('created_at', formatDateForServer(solution.createdAt)); 
          formData.append('updated_at', formatDateForServer(solution.updatedAt)); 
  
          if (solution.solution_image) {
            formData.append('solution_image', solution.solution_image);
          }
  
          const response = await axios.post('http://127.0.0.1:8000/api/solutions/create/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
  
          console.log(response.data);
  
          Object.keys(solution).forEach(key => {
            solution[key] = '';
          });
  
          fetchSolutions();
  
        } catch (error) {
          console.error('Error submitting solution:', error);
        }
      };
  
      const deleteSolution = async (id) => {
        try {
          await axios.delete(`http://127.0.0.1:8000/api/solutions/${id}/delete`);
          fetchSolutions();
        } catch (error) {
          console.error('Error deleting solution:', error);
        }
      };
  
      const updateSolutionForm = (solutionData) => {
        solution.id=solutionData.id
        solution.name = solutionData.name;
        solution.description = solutionData.description;
        solution.ctatext = solutionData.ctatext;
        solution.created_by = solutionData.created_by;
        solution.createdAt = formatDate(solutionData.createdAt);
        solution.updatedAt = formatDate(solutionData.updatedAt);
        solution.entity = solutionData.entity;
        solution.solution_image = solutionData.solution_image;
      };
  
      const updateSolutiononSubmit = async () => {
  try {
    const id = solution.id; // Get the id from the solution object
    const formData = new FormData();
    formData.append('name', solution.name);
    formData.append('description', solution.description);
    formData.append('ctatext', solution.ctatext);
    formData.append('created_by', solution.created_by);
    formData.append('entity', solution.entity);
    formData.append('created_at', formatDateForServer(solution.createdAt)); 
    formData.append('updated_at', formatDateForServer(solution.updatedAt)); 

    if (solution.solution_image) {
      formData.append('solution_image', solution.solution_image);
    }

    const response = await axios.put(`http://127.0.0.1:8000/api/solutions/${id}/update/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    console.log(response.data);

    Object.keys(solution).forEach(key => {
      solution[key] = '';
    });

    fetchSolutions();

  } catch (error) {
    console.error('Error updating solution:', error);
  }
};

  
      const handleImageUpload = (event) => {
        solution.solution_image = event.target.files[0];
      };
  
      const getEntityName = (entityId) => {
        const entity = entities.value.find(entity => entity.id === entityId);
        return entity ? entity.name : '';
      };
    
      const formatDate = (dateString) => {
        return dateString ? new Date(dateString).toISOString().split('T')[0] : ''; // Format the date string to remove time
      };
    
      const formatDateForServer = (dateString) => {
  return dateString ? dateString.split('T')[0] : ''; // Remove the time part of the ISO string
};
  
      onMounted(() => {
        fetchEntities();
        fetchSolutions();
      });
  
      return {
        solution,
        entities,
        solutions,
        submitSolution,
        handleImageUpload,
        deleteSolution,
        updateSolutionForm,
        getEntityName,
        updateSolutiononSubmit
      };
    }
  };
  </script>
  
  <style scoped>
  .card {
    margin-bottom: 20px;
  }
  </style>