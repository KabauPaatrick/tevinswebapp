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
                  <th>Slug</th>
                  <th>Price</th>
                  <th>Category</th>
                  <th>Brand</th>
                  <th>Quantity</th>
                  <th>Colors</th>
                  <th>Tags</th>
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
                  <td>{{ product.slug }}</td>
                  <td>{{ product.price }}</td>
                  <td>{{ getCategoryName(product.category) }}</td>
                  <td>{{ getBrandName(product.brand) }}</td>
                  <td>{{ product.quantity }}</td>
                  <td>{{ getColorNames(product.colors) }}</td>
                  <td>{{ Array.isArray(product.tags) ? product.tags.join(', ') : '' }}</td>
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

export default {
  name: 'NewAdminPage',
  components: {
    AdminNav,
  },
  setup() {
    const product = reactive({
      id: '',
      title: '',
      description: '',
      slug: '',
      price: '',
      category: '',
      brand: '',
      quantity: 0,
      colors: [],
      tags: [],
      image: null,
      images: []
    });

    const products = ref([]);
    const categories = ref([]);
    const brands = ref([]);
    const colors = ref([]);
    const tagsInput = ref(''); // For handling tags input

    const currentPage = ref(1);
    const itemsPerPage = 10;

    const paginatedProducts = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return products.value.slice(start, end);
    });

    const totalPages = computed(() => {
      return Math.ceil(products.value.length / itemsPerPage);
    });

    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        currentPage.value = page;
      }
    };

    const fetchOptions = async () => {
      try {
        const [categoriesRes, brandsRes, colorsRes] = await Promise.all([
          axios.get('http://127.0.0.1:8000/api/category/list/'),
          axios.get('http://127.0.0.1:8000/api/brand/show/'),
          axios.get('http://127.0.0.1:8000/api/color/show/')
        ]);

        categories.value = categoriesRes.data;
        brands.value = brandsRes.data;
        colors.value = colorsRes.data;
      } catch (error) {
        console.error('Error fetching options:', error);
      }
    };

    const handleImageUpload = (event) => {
      product.image = event.target.files[0]; // Single image upload
    };

    const handleAdditionalImagesUpload = (event) => {
      product.images = Array.from(event.target.files); // Multiple images upload
    };

    const updateTags = () => {
      product.tags = tagsInput.value.split(',').map(tag => tag.trim());
    };

    const createProduct = async () => {
      try {
        const formData = new FormData();
        formData.append('title', product.title);
        formData.append('description', product.description);
        formData.append('slug', product.slug);
        formData.append('price', product.price);
        formData.append('category', product.category);
        formData.append('brand', product.brand);
        formData.append('quantity', product.quantity);
        formData.append('colors', product.colors);
        formData.append('tags', JSON.stringify(product.tags));
        formData.append('image', product.image); // Single image

        product.images.forEach((image, index) => {
          formData.append(`images[${index}]`, image); // Multiple images
        });

        const response = await axios.post('http://127.0.0.1:8000/api/products/create/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('Product created:', response.data);
        products.value.push(response.data);
        resetForm();
      } catch (error) {
        console.error('Error creating product:', error);
      }
    };

    const deleteProduct = async (id) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/products/delete/${id}/`);
        products.value = products.value.filter(product => product.id !== id);
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    };

    const updateProductForm = (selectedProduct) => {
  product.id = selectedProduct.id;
  product.title = selectedProduct.title;
  product.description = selectedProduct.description;
  product.slug = selectedProduct.slug;
  product.price = selectedProduct.price;
  product.category = selectedProduct.category;
  product.brand = selectedProduct.brand;
  product.quantity = selectedProduct.quantity;
  product.colors = selectedProduct.colors;
  product.tags = selectedProduct.tags;
  product.image = null; // Reset to null for new image upload
  product.images = []; // Reset to empty for new additional images upload
};

    const updateProduct = async () => {
      try {
        const formData = new FormData();
        formData.append('title', product.title);
        formData.append('description', product.description);
        formData.append('slug', product.slug);
        formData.append('price', product.price);
        formData.append('category', product.category);
        formData.append('brand', product.brand);
        formData.append('quantity', product.quantity);
        formData.append('colors', JSON.stringify(product.colors));
        formData.append('tags', JSON.stringify(product.tags));
        if (product.image) {
          formData.append('image', product.image); // Only append if a new image is uploaded
        }
        product.images.forEach((image, index) => {
          formData.append(`images[${index}]`, image); // Append new additional images
        });

        const response = await axios.put(`http://127.0.0.1:8000/api/products/update/${product.id}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('Product updated:', response.data);
        const index = products.value.findIndex(prod => prod.id === product.id);
        if (index !== -1) {
          products.value[index] = response.data;
        }
        resetForm();
      } catch (error) {
        console.error('Error updating product:', error);
      }
    };

    const getCategoryName = (categoryId) => {
      const category = categories.value.find(category => category.id === categoryId);
      return category ? category.title : 'Unknown';
    };

    const getBrandName = (brandId) => {
      const brand = brands.value.find(brand => brand.id === brandId);
      return brand ? brand.title : 'Unknown';
    };

    const getColorNames = (colorIds) => {
      const colorNames = colors.value
        .filter(color => colorIds.includes(color.id))
        .map(color => color.title);
      return colorNames.join(', ');
    };

    const resetForm = () => {
      product.id = '';
      product.title = '';
      product.description = '';
      product.slug = '';
      product.price = '';
      product.category = '';
      product.brand = '';
      product.quantity = 0;
      product.colors = [];
      product.tags = [];
      product.image = null;
      product.images = [];
    };

    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/list/');
        products.value = response.data;
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    // Fetch data when component is mounted
    fetchOptions();
    fetchProducts();

    return {
      product,
      products,
      categories,
      brands,
      colors,
      tagsInput,
      createProduct,
      deleteProduct,
      updateProductForm,
      updateProduct,
      getCategoryName,
      getBrandName,
      getColorNames,
      paginatedProducts,
      currentPage,
      totalPages,
      changePage,
      handleImageUpload,
      handleAdditionalImagesUpload,
      updateTags,
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

img {
  max-width: 100%;
  height: auto;
}
</style>
