<template>
  <div>
    <AdminNav />
    <div class="container mt-5">
      <!-- Product Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Create New Product</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="createProduct" class="form">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="title" class="form-label">Title:</label>
                  <input type="text" id="title" v-model="product.title" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="description" class="form-label">Description:</label>
                  <textarea id="description" v-model="product.description" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="details" class="form-label">Product Details:</label>
                  <textarea id="details" v-model="product.details" class="form-control" required></textarea>
                </div>
                <div class="form-group">
                  <label for="slug" class="form-label">Slug:</label>
                  <input type="text" id="slug" v-model="product.slug" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="price" class="form-label">Price:</label>
                  <input type="number" id="price" v-model="product.price" step="0.01" class="form-control" required>
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <label for="category" class="form-label">Category:</label>
                  <select id="category" v-model="product.category" class="form-control" required>
                    <option v-for="category in categories" :key="category.id" :value="category.id">
                      {{ category.title }}
                    </option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="brand" class="form-label">Brand:</label>
                  <select id="brand" v-model="product.brand" class="form-control" required>
                    <option v-for="brand in brands" :key="brand.id" :value="brand.id">
                      {{ brand.title }}
                    </option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="quantity" class="form-label">Quantity:</label>
                  <input type="number" id="quantity" v-model="product.quantity" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="colors" class="form-label">Colors:</label>
                  <select id="colors" v-model="product.colors" class="form-control" multiple>
                    <option v-for="color in colors" :key="color.id" :value="color.id">
                      {{ color.title }}
                    </option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="tags" class="form-label">Tags:</label>
                  <input type="text" id="tags" v-model="tagsInput" class="form-control" @input="updateTags">
                </div>
                <div class="form-group">
                  <label for="location" class="form-label">Location:</label>
                  <TreeSelect
                    v-model="product.location"
                    :options="locationOptions"
                    placeholder="Select Location"
                    class="form-control"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="dropoff" class="form-label">Dropoff Point:</label>
                  <TreeSelect
                    v-model="product.dropoff"
                    :options="dropoffOptions"
                    placeholder="Select Dropoff Point"
                    class="form-control"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12">
                <div class="form-group">
                  <label for="image" class="form-label">Main Image:</label>
                  <input type="file" id="image" @change="handleImageUpload" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="additionalImages" class="form-label">Additional Images:</label>
                  <input type="file" id="additionalImages" @change="handleAdditionalImagesUpload" multiple class="form-control">
                </div>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Create Product</button>
                <button type="button" class="btn btn-primary" @click="updateProduct">Update</button>
              </div>
            </div>
          </form>
        </div>
      </div>

      <!-- Product Table -->
      <div class="card">
        <div class="card-header">
          <h2 class="mb-0">Product List</h2>
        </div>
        <div class="card-body">
          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>Image</th>
                  <th>Title</th>
                  <th>Description</th>
                  <th>Details</th>
                  <th>Slug</th>
                  <th>Price</th>
                  <th>Category</th>
                  <th>Brand</th>
                  <th>Quantity</th>
                  <th>Colors</th>
                  <th>Tags</th>
                  <th>Location</th>
                  <th>Dropoff Point</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(product, index) in paginatedProducts" :key="index">
                  <td>
                    <img :src="product.image" alt="Product Image" style="width: 100px; height: auto;">
                  </td>
                  <td>{{ product.title }}</td>
                  <td>{{ product.description }}</td>
                  <td>{{ product.details }}</td>
                  <td>{{ product.slug }}</td>
                  <td>{{ product.price }}</td>
                  <td>{{ getCategoryName(product.category) }}</td>
                  <td>{{ getBrandName(product.brand) }}</td>
                  <td>{{ product.quantity }}</td>
                  <td>{{ getColorNames(product.colors) }}</td>
                  <td>{{ Array.isArray(product.tags) ? product.tags.join(', ') : '' }}</td>
                  <td>{{ getLocationName(product.location) }}</td>
                  <td>{{ getDropoffName(product.dropoff) }}</td>
                  <td class="d-flex">
                    <button @click="deleteProduct(product.id)" class="btn btn-danger mr-2">Delete</button>
                    <button @click="updateProductForm(product)" class="btn btn-primary">Update</button>
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
import TreeSelect from 'vue-tree-select';

export default {
  name: 'NewAdminPage',
  components: {
    AdminNav,
    TreeSelect,
  },
  setup() {
    const product = reactive({
      id: '',
      title: '',
      description: '',
      details:'',
      slug: '',
      price: '',
      category: '',
      brand: '',
      quantity: 0,
      colors: [],
      tags: [],
      image: null,
      images: [],
      location: null,
      dropoff: null,
    });

    const products = ref([]);
    const categories = ref([]);
    const brands = ref([]);
    const colors = ref([]);
    const tagsInput = ref('');
    const locationOptions = ref([]);
    const dropoffOptions = ref([]);

    const currentPage = ref(1);
    const itemsPerPage = 10;

    const paginatedProducts = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start +  itemsPerPage;
      return products.value.slice(start, end);
    });

    const totalPages = computed(() => {
      return Math.ceil(products.value.length / itemsPerPage);
    });

    const fetchCategories = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/category/list/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        categories.value = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    const fetchBrands = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/brand/show/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        brands.value = response.data;
      } catch (error) {
        console.error('Error fetching brands:', error);
      }
    };

    const fetchColors = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/color/show/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        colors.value = response.data;
      } catch (error) {
        console.error('Error fetching colors:', error);
      }
    };

    const fetchLocations = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/location/locations/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        locationOptions.value = response.data;
      } catch (error) {
        console.error('Error fetching locations:', error);
      }
    };

    const fetchDropoffs = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/location/dropoff-points/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        dropoffOptions.value = response.data;
      } catch (error) {
        console.error('Error fetching dropoffs:', error);
      }
    };

    const fetchProducts = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/products/', {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        products.value = response.data;
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    const createProduct = async () => {
      const formData = new FormData();
      formData.append('title', product.title);
      formData.append('description', product.description);
      formData.append('details', product.details);
      formData.append('slug', product.slug);
      formData.append('price', product.price);
      formData.append('category', product.category);
      formData.append('brand', product.brand);
      formData.append('quantity', product.quantity);
      formData.append('colors', product.colors.join(','));
      formData.append('tags', product.tags.join(','));
      formData.append('location', product.location);
      formData.append('dropoff', product.dropoff);
      if (product.image) {
        formData.append('image', product.image);
      }
      for (let i = 0; i < product.images.length; i++) {
        formData.append('images', product.images[i]);
      }

      try {
        await axios.post('https://kabau.pythonanywhere.com/api/products/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        fetchProducts(); // Refresh the product list
      } catch (error) {
        console.error('Error creating product:', error);
      }
    };

    const handleImageUpload = (event) => {
      product.image = event.target.files[0];
    };

    const handleAdditionalImagesUpload = (event) => {
      product.images = Array.from(event.target.files);
    };

    const updateProduct = async () => {
      // Implement product update logic here
    };

    const deleteProduct = async (id) => {
      try {
        await axios.delete(`https://kabau.pythonanywhere.com/api/products/${id}/`, {
          headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` }
        });
        fetchProducts(); // Refresh the product list
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    };

    const updateProductForm = (productData) => {
      Object.assign(product, productData);
    };

    const changePage = (page) => {
      if (page > 0 && page <= totalPages.value) {
        currentPage.value = page;
      }
    };

    const getCategoryName = (id) => {
      const category = categories.value.find(cat => cat.id === id);
      return category ? category.title : '';
    };

    const getBrandName = (id) => {
      const brand = brands.value.find(b => b.id === id);
      return brand ? brand.title : '';
    };

    const getColorNames = (ids) => {
      return ids.map(id => {
        const color = colors.value.find(c => c.id === id);
        return color ? color.title : '';
      }).join(', ');
    };

    const getLocationName = (id) => {
      const location = locationOptions.value.find(loc => loc.id === id);
      return location ? location.title : '';
    };

    const getDropoffName = (id) => {
      const dropoff = dropoffOptions.value.find(d => d.id === id);
      return dropoff ? dropoff.title : '';
    };

    const updateTags = (event) => {
      const tags = event.target.value.split(',').map(tag => tag.trim()).filter(tag => tag);
      product.tags = tags;
    };

    // Fetch initial data
    fetchCategories();
    fetchBrands();
    fetchColors();
    fetchLocations();
    fetchDropoffs();
    fetchProducts();

    return {
      product,
      products,
      categories,
      brands,
      colors,
      tagsInput,
      locationOptions,
      dropoffOptions,
      paginatedProducts,
      totalPages,
      currentPage,
      createProduct,
      handleImageUpload,
      handleAdditionalImagesUpload,
      updateProduct,
      deleteProduct,
      updateProductForm,
      changePage,
      getCategoryName,
      getBrandName,
      getColorNames,
      getLocationName,
      getDropoffName,
      updateTags,
    };
  },
};
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.card {
  margin-bottom: 20px;
}

.page-item.disabled .page-link {
  pointer-events: none;
  cursor: default;
}

.page-item.active .page-link {
  background-color: #007bff;
  border-color: #007bff;
  color: #fff;
}

.page-link {
  cursor: pointer;
}
</style>

