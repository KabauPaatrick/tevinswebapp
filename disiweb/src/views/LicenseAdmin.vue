<template>
  <div>
    <AdminNav />
    <Admintop />
    <div class="container mt-5">
      <!-- Solution Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Add a New License</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="submitLicense" class="form">
            <div class="row">
              <div class="col-md-6">
                <!-- Input fields for solution -->
                <div class="form-group">
                  <label for="name" class="form-label">Name:</label>
                  <input type="text" id="name" v-model="license.name" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="description" class="form-label">Description:</label>
                  <textarea id="description" v-model="license.description" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="ctatext" class="form-label">CTA Text:</label>
                  <input type="text" id="ctatext" v-model="license.ctatext" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="createdBy" class="form-label">Created By:</label>
                  <input type="text" id="createdBy" v-model="license.created_by" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="createdAt" class="form-label">Created At:</label>
                  <input type="date" id="createdAt" v-model="license.createdAt" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="updatedAt" class="form-label">Updated At:</label>
                  <input type="date" id="updatedAt" v-model="license.updatedAt" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <!-- Input fields for solution -->
                <div class="form-group">
                  <label for="licenseImage" class="form-label">Image:</label>
                  <input type="file" id="licenseImage" @change="handleImageUpload" class="form-control" accept="image/*" required>
                </div>
                <!-- Entity field -->
                <div class="form-group">
                  <label for="entity" class="form-label">Entity:</label>
                  <select v-model="license.entity" id="entity" class="form-control" required>
                    <option v-for="entity in entities" :key="entity.id" :value="entity.id">{{ entity.name }}</option>
                  </select>
                </div>
              </div>
            </div>
            <!-- Submit and update buttons -->
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Add License</button>
                <button type="button" class="btn btn-primary" @click="updateLicenseonSubmit(license.id)">Update Solution</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- Solution Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">License List</h2>
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
                <tr v-for="(license, index) in licenses" :key="index">
                  <td>{{ license.name }}</td>
                  <td>{{ license.description }}</td>
                  <td>{{ license.ctatext }}</td>
                  <td><img :src="license.license_images" alt="License Image" style="max-width: 100px;"></td>
                  <td>{{ license.createdBy }}</td>
                  <td>{{ formatDate(license.createdAt) }}</td>
                  <td>{{ formatDate(license.updatedAt) }}</td>
                  <td>{{ getEntityName(license.entity) }}</td>
                  <td class="d-flex">
                    <button @click="deleteLicense(license.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateLicenseForm(license)" class="btn btn-primary">Update</button>
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
import Admintop from '@/components/Admintop.vue';

const formatDate = (dateString) => {
  return new Date(dateString).toISOString().split('T')[0]; // Format the date string to remove time
};
export default {
  name: 'NewAdminNPage', 
    components: {
      AdminNav,
      Admintop
    },
  setup() {
    const license = reactive({
      name: '',
      description: '',
      ctatext: '',
      licenseImage: null, // Changed name to match file input
      created_by: '',
      createdAt: null,
      updatedAt: null,
      entity: '',
    });

    const entities = ref([]);
    const licenses = ref([]);

    const fetchEntities = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/entity/show/');
        entities.value = response.data;
      } catch (error) {
        console.error('Error fetching entities:', error);
      }
    };

    const fetchLicense = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/license/show/');
        licenses.value = response.data.map(license => ({
          ...license,
          createdAt: formatDate(license.created_at),
          updatedAt: formatDate(license.updated_at)
        }));
      } catch (error) {
        console.error('Error fetching licenses:', error);
      }
    };

    const submitLicense = async () => {
      try {
        const formData = new FormData();
        formData.append('name', license.name);
        formData.append('description', license.description);
        formData.append('ctatext', license.ctatext);
        formData.append('created_by', license.created_by);
        formData.append('entity', license.entity);
        formData.append('created_at', formatDateForServer(license.createdAt));
        formData.append('updated_at', formatDateForServer(license.updatedAt));

        if (license.licenseImage) {
          formData.append('license_images', license.licenseImage);
        }

        const response = await axios.post('https://kabau.pythonanywhere.com/api/license/create/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        console.log(response.data);

        Object.keys(license).forEach(key => {
          license[key] = '';
        });

        fetchLicense();

      } catch (error) {
        console.error('Error submitting license:', error);
      }
    };

    const deleteLicense = async (id) => {
      try {
        await axios.delete(`https://kabau.pythonanywhere.com/api/license/${id}/delete`);
        fetchLicense();
      } catch (error) {
        console.error('Error deleting license:', error);
      }
    };

    const updateLicenseForm = (licenseData) => {
      license.name = licenseData.name;
      license.description = licenseData.description;
      license.ctatext = licenseData.ctatext;
      license.created_by = licenseData.created_by;
      license.createdAt = licenseData.created_at; // No need to format since it's already formatted
      license.updatedAt = licenseData.updated_at; // No need to format since it's already formatted
      license.entity = licenseData.entity;
      license.licenseImage = licenseData.license_images; // Changed name to match file input
    };

    const updateLicenseonSubmit = async (id) => {
      try {
        const formData = new FormData();
        formData.append('name', license.name);
        formData.append('description', license.description);
        formData.append('ctatext', license.ctatext);
        formData.append('created_by', license.created_by);
        formData.append('entity', license.entity);
        formData.append('created_at', formatDateForServer(license.createdAt));
        formData.append('updated_at', formatDateForServer(license.updatedAt));

        if (license.licenseImage) {
          formData.append('license_images', license.licenseImage);
        }

        const response = await axios.put(`https://kabau.pythonanywhere.com/api/license/${id}/update/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        console.log(response.data);

        Object.keys(license).forEach(key => {
          license[key] = '';
        });

        fetchLicense();

      } catch (error) {
        console.error('Error updating license:', error);
      }
    };

    const handleImageUpload = (event) => {
      license.licenseImage = event.target.files[0];
    };

    const getEntityName = (entityId) => {
      const entity = entities.value.find(entity => entity.id === entityId);
      return entity ? entity.name : '';
    };

    const formatDateForServer = (dateString) => {
      return dateString; // No need to format since it's already in the correct format
    };

    onMounted(() => {
      fetchEntities();
      fetchLicense();
    });

    return {
      license,
      entities,
      licenses,
      submitLicense,
      handleImageUpload,
      deleteLicense,
      updateLicenseForm,
      formatDate,
      updateLicenseonSubmit,
      getEntityName
    };
  }
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}
</style>
