<template>
  <div>
    <AdminNav />
    <div class="container mt-5">
      <!-- New Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Entity</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="createEntry" class="form">
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
                <div class="form-group">
                  <label for="contactPerson" class="form-label">Contact Person:</label>
                  <input type="text" id="contactPerson" v-model="entity.contactPerson" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="email" class="form-label">Email:</label>
                  <input type="email" id="email" v-model="entity.email" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="phoneNumber" class="form-label">Phone Number:</label>
                  <input type="text" id="phoneNumber" v-model="entity.phoneNumber" class="form-control" required>
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Create Entry</button>
                <button type="button" class="btn btn-primary" @click="updateEntry(entity)">Update</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- Entry Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Entry List</h2>
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
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(entity, index) in paginatedEntries" :key="index">
                  <td>{{ entity.name }}</td>
                  <td>{{ entity.description }}</td>
                  <td>{{ entity.location }}</td>
                  <td>{{ entity.contactPerson }}</td>
                  <td>{{ entity.email }}</td>
                  <td>{{ entity.phoneNumber }}</td>
                  <td class="d-flex">
                    <button @click="deleteEntry(entity.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateEntryForm(entity)" class="btn btn-primary">Update</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <!-- Pagination Controls -->
          <nav aria-label="Page navigation example">
            <ul class="pagination">
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage - 1)">Previous</a>
              </li>
              <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: page === currentPage }">
                <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
              </li>
              <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                <a class="page-link" href="#" @click.prevent="changePage(currentPage + 1)">Next</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref, computed } from 'vue';
import axios from 'axios';
import AdminNav from '@/components/AdminNav.vue';

export default {
  name: 'NewAdminPage',
  components: {
    AdminNav,
  },
  setup() {
    const entity = reactive({
      id: '',
      name: '',
      description: '',
      location: '',
      contactPerson: '',
      email: '',
      phoneNumber: ''
    });

    const entries = ref([]);
    const currentPage = ref(1);
    const itemsPerPage = 10;

    const paginatedEntries = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return entries.value.slice(start, end);
    });

    const totalPages = computed(() => {
      return Math.ceil(entries.value.length / itemsPerPage);
    });

    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page;
      }
    };

    const createEntry = async () => {
      try {
        const response = await axios.post('https://kabau.pythonanywhere.com/api/entity/create/', entity);
        console.log('Entry created successfully:', response.data);
        fetchEntries(); // Fetch and update the entity list
      } catch (error) {
        console.error('Error creating entity:', error);
      }
    };

    const fetchEntries = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/entity/show/');
        entries.value = response.data;
      } catch (error) {
        console.error('Error fetching entries:', error);
      }
    };

    const deleteEntry = async (entryId) => {
      try {
        await axios.delete(`https://kabau.pythonanywhere.com/api/entity/${entryId}/`);
        fetchEntries(); // Refresh entries after deletion
      } catch (error) {
        console.error('Error deleting entity:', error);
      }
    };

    const updateEntryForm = (entryData) => {
      Object.assign(entity, entryData);
    };

    const updateEntry = async (entryData) => {
      try {
        if (!entryData.id) {
          console.error('entryData is undefined or does not have an id');
          return;
        }

        const response = await axios.put(`https://kabau.pythonanywhere.com/api/entity/${entryData.id}/update/`, entity);
        console.log('Entry updated successfully:', response.data);
        fetchEntries(); // Fetch updated entries
      } catch (error) {
        console.error('Error updating entity:', error);
      }
    };

    fetchEntries();

    return {
      entity,
      entries,
      createEntry,
      deleteEntry,
      updateEntryForm,
      updateEntry,
      paginatedEntries,
      currentPage,
      totalPages,
      changePage
    };
  },
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}

.form-label {
  font-weight: bold;
}

.form-control {
  margin-bottom: 10px;
}

.table th, .table td {
  vertical-align: middle;
}

.btn {
  margin-right: 10px;
}
</style>
