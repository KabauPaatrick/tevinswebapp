<template>
  <div>
    <AdminNav />
    <div class="container mt-5">
      <!-- Entity Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Entity</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="submitEntity" class="form">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="name" class="form-label">Name:</label>
                  <input type="text" id="name" v-model="entity.name" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="description" class="form-label">Description:</label>
                  <textarea id="description" v-model="entity.description" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="location" class="form-label">Location:</label>
                  <input type="text" id="location" v-model="entity.location" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="contactPerson" class="form-label">Contact Person:</label>
                  <input type="text" id="contact_person" v-model="entity.contact_person" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="email" class="form-label">Email:</label>
                  <input type="email" id="email" v-model="entity.email" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="phoneNumber" class="form-label">Phone Number:</label>
                  <input type="tel" id="phone_number" v-model="entity.phone_number" class="form-control" required>
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Add Entity</button>
                <!-- Update button placed inline with Add button -->
                <button type="button" class="btn btn-primary" @click="updateEntity(entity)">Update</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- Entity Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Entity List</h2>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Description</th>
                  <th>Location</th>
                  <th>Contact Person</th>
                  <th>Email</th>
                  <th>Phone Number</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(entity, index) in entities" :key="index">
                  <td>{{ entity.name }}</td>
                  <td>{{ entity.description }}</td>
                  <td>{{ entity.location }}</td>
                  <td>{{ entity.contact_person }}</td>
                  <td>{{ entity.email }}</td>
                  <td>{{ entity.phone_number }}</td>
                  <td class="d-flex">
                    <button @click="deleteEntity(entity.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateEntityForm(entity)" class="btn btn-primary">Update</button>
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
import { reactive } from 'vue';
import axios from 'axios';
import AdminNav from '@/components/AdminNav.vue';

export default {
  name: 'NewAdminNPage', // Correct component name
    components: {
      AdminNav,
    },
  setup() {
    const entity = reactive({
      id: '',
      name: '',
      description: '',
      location: '',
      contact_person: '',
      email: '',
      phone_number: '',
    });

    const entities = reactive([]);

    const submitEntity = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/entity/create/', entity);
        console.log(response.data);
        // Reset entity fields after submission
        Object.keys(entity).forEach(key => {
          entity[key] = '';
        });
        // Fetch and update the entities list
        fetchEntities();
      } catch (error) {
        console.error('Error submitting entity:', error);
      }
    };


    const updateEntityForm = (entityData) => {
      entity.id = entityData.id
      entity.name = entityData.name;
      entity.description = entityData.description;
      entity.location = entityData.location;
      entity.contact_person = entityData.contact_person;
      entity.email = entityData.email;
      entity.phone_number = entityData.phone_number;

    };
    const updateEntity = async (entityData) => {
    try {
        if (!entityData.id) {
            console.error('entityData is undefined or does not have an id');
            return;
        }
        
        const response = await axios.put(`http://127.0.0.1:8000/api/entity/${entityData.id}/update/`, entityData);
        console.log(response.data);
        
        // Reset entity fields after updating
        Object.keys(entity).forEach(key => {
            entity[key] = '';
        });
        
        // Fetch updated entities
        await fetchEntities();
    } catch (error) {
        console.error('Error updating an entity:', error);
    }

    // Logic for updating the entity
    console.log('Update button clicked');
};


    const fetchEntities = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/entity/show/');
        entities.splice(0); // Clear the existing entities array
        entities.push(...response.data); // Add fetched entities to the array
      } catch (error) {
        console.error('Error fetching entities:', error);
      }
    };
    const deleteEntity = async (entityId) => {
  try {
    await axios.delete(`http://127.0.0.1:8000/api/entity/${entityId}/delete/`);
    await fetchEntities(); // Refresh entities after deletion
  } catch (error) {
    console.error('Error deleting entity:', error);
  }
};

    return {
      entity,
      entities,
      submitEntity,
      updateEntity,
      fetchEntities,
      updateEntityForm,
      deleteEntity
    };
  },
  mounted() {
    this.fetchEntities(); // Fetch entities on component mount
  }
};
</script>

<style scoped>
/* Add custom styles here if needed */
.card {
  margin-bottom: 20px;
}
</style>
