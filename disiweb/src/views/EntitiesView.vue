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
                      {{ category.name }}
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
                  <input type="text" id="tags" v-model="tags" class="form-control" @input="updateTags">
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
                <button type="button" class="btn btn-primary" @click="updateProduct(product)">Update</button>
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
                  <td>{{ product.tags ? product.tags.join(', ') : '' }}</td>
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
    const tags = ref('');

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
      product.image = URL.createObjectURL(event.target.files[0]);
    };

    const handleAdditionalImagesUpload = (event) => {
      product.images = Array.from(event.target.files).map(file => URL.createObjectURL(file));
    };

    const updateTags = (event) => {
      product.tags = event.target.value.split(',').map(tag => tag.trim());
    };

    const createProduct = async () => {
      const formData = new FormData();
      for (const key in product) {
        if (key === 'images') {
          product.images.forEach((image, index) => {
            formData.append(`image_files[${index}]`, image);
          });
        } else {
          formData.append(key, product[key]);
        }
      }

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/products/create/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Product created successfully:', response.data);
        fetchProducts(); // Fetch and update the product list
      } catch (error) {
        console.error('Error creating product:', error);
      }
    };

    const fetchProducts = async () => {
      try {
        const response = await axios.get('https://kabau.pythonanywhere.com/api/products/');
        products.value = response.data;
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    const deleteProduct = async (productId) => {
      try {
        await axios.delete(`https://kabau.pythonanywhere.com/api/products/${productId}/`);
        fetchProducts(); // Refresh products after deletion
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    };

    const updateProductForm = (productData) => {
      Object.assign(product, productData);
      tags.value = product.tags.join(', ');
    };

    const updateProduct = async (productData) => {
      try {
        if (!productData.id) {
          console.error('productData is undefined or does not have an id');
          return;
        }

        const formData = new FormData();
        for (const key in product) {
          if (key === 'images') {
            product.images.forEach((image, index) => {
              formData.append(`image_files[${index}]`, image);
            });
          } else {
            formData.append(key, product[key]);
          }
        }

        const response = await axios.put(`https://kabau.pythonanywhere.com/api/products/${productData.id}/update/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log('Product updated successfully:', response.data);
        fetchProducts(); // Fetch updated products
      } catch (error) {
        console.error('Error updating product:', error);
      }
    };

    const getCategoryName = (categoryId) => {
      const category = categories.value.find((cat) => cat.id === categoryId);
      return category ? category.name : '';
    };

    const getBrandName = (brandId) => {
      const brand = brands.value.find((br) => br.id === brandId);
      return brand ? brand.name : '';
    };

    const getColorNames = (colorIds) => {
      const colorNames = colorIds.map((colorId) => {
        const color = colors.value.find((col) => col.id === colorId);
        return color ? color.name : '';
      });
      return colorNames.join(', ');
    };

    fetchOptions();
    fetchProducts();

    return {
      product,
      products,
      categories,
      brands,
      colors,
      tags,
      handleImageUpload,
      handleAdditionalImagesUpload,
      updateTags,
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

img {
  max-width: 100%;
  height: auto;
}
</style>
