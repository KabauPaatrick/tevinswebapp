<template>
  <div class="edit-body">
    <div class="edit-product">
      <h1>EDIT PRODUCT</h1>
      <hr class="solid">
      <div class="edit-data">
        <form class="file-upload-form">
          <label for="file" class="file-upload-label">
            <div class="file-upload-design">
              <span class="material-symbols-outlined upload-icon">upload_file</span>
              <p>Drag and Drop</p>
              <p>or</p>
              <span class="browse-button">Browse file(s)</span>
            </div>
            <input id="file" type="file" @change="handleFileUpload"/>
          </label>
        </form>
        <form class="edit-details">
          <input type="text" placeholder="Product Name" v-model="product.title" required>
          <input type="text" placeholder="Enter Price" v-model="product.price" required>
          <input type="text" placeholder="Enter Slug" v-model="product.slug" required>
          <textarea name="Prod-details" id="Prod-details" placeholder="Enter Product Details" v-model="product.description" required></textarea>
          <select v-model="product.category" required>
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.title }}
            </option>
          </select>
          <select v-model="product.brand" required>
            <option v-for="brand in brands" :key="brand.id" :value="brand.id">
              {{ brand.title }}
            </option>
          </select>
          <input type="number" placeholder="Enter Quantity" v-model="product.quantity" required>
          <select v-model="product.colors" multiple required>
            <option v-for="color in colors" :key="color.id" :value="color.id">
              {{ color.title }}
            </option>
          </select>
          <input type="text" placeholder="Enter Tags" v-model="tagsInput" @input="updateTags">
          <button id="submit-edit" @click.prevent="editProduct">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EditProduct',
  data() {
    return {
      product: {
        title: '',
        description: '',
        slug: '',
        price: '',
        category: '',
        brand: '',
        quantity: 0,
        colors: [],
        tags: [],
      },
      selectedFile: null,
      categories: [],
      brands: [],
      colors: [],
      tagsInput: '',
    };
  },
  mounted() {
    this.fetchProduct();
    this.fetchOptions();
  },
  methods: {
    async fetchProduct() {
      const productId = this.$route.params.id;
      const productUrl = `http://127.0.0.1:8000/api/products/${productId}/`;
      try {
        const response = await axios.get(productUrl);
        this.product = response.data;
        this.tagsInput = this.product.tags.join(', ');
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    },
    async fetchOptions() {
      try {
        const [categoriesRes, brandsRes, colorsRes] = await Promise.all([
          axios.get('http://127.0.0.1:8000/api/category/list/'),
          axios.get('http://127.0.0.1:8000/api/brand/show/'),
          axios.get('http://127.0.0.1:8000/api/color/show/')
        ]);

        this.categories = categoriesRes.data;
        this.brands = brandsRes.data;
        this.colors = colorsRes.data;
      } catch (error) {
        console.error('Error fetching options:', error);
      }
    },
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
    },
    updateTags() {
      this.product.tags = this.tagsInput.split(',').map(tag => tag.trim());
    },
    async editProduct() {
      const productId = this.$route.params.id;
      const productUrl = `http://127.0.0.1:8000/api/products/${productId}/update/`;

      try {
        const formData = new FormData();
        formData.append('title', this.product.title);
        formData.append('description', this.product.description);
        formData.append('slug', this.product.slug);
        formData.append('price', this.product.price);
        formData.append('category', this.product.category);
        formData.append('brand', this.product.brand);
        formData.append('quantity', this.product.quantity);
        this.product.colors.forEach(color => formData.append('colors', color));
        formData.append('tags', JSON.stringify(this.product.tags));
        if (this.selectedFile) {
          formData.append('image', this.selectedFile);
        }

        const response = await axios.put(productUrl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        console.log('Product updated:', response.data);
        this.$router.push('/products'); // Redirect to products page after successful update
      } catch (error) {
        console.error('Error updating product:', error);
      }
    }
  }
};
</script>


<style scoped>
.edit-body {
  background: #cacbd5;
  display: flex;
  flex-direction: column;
  margin: auto;
  margin-top: 30px;
  width: 70vw;
  border-radius: 10px;
  padding: 10px;
}

h1 {
  font-size: 30px;
  margin-bottom: 0;
  color: black;
}

.edit-product {
  display: flex;
  flex-direction: column;
}

.edit-data {
  display: flex;
  gap: 30px;
}

.edit-details {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 50%;
}

.file-upload-form {
  width: fit-content;
  height: fit-content;
  display: flex;
  align-items: center;
  justify-content: center;
}

.file-upload-label input {
  display: none;
}

.upload-icon {
  font-size: 50px;
}

.file-upload-label {
  cursor: pointer;
  background-color: #ddd;
  padding: 30px 70px;
  border-radius: 40px;
  border: 2px dashed rgb(82, 82, 82);
  box-shadow: 0px 0px 200px -50px rgba(0, 0, 0, 0.719);
}

.file-upload-design {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.browse-button {
  background-color: rgb(82, 82, 82);
  padding: 5px 15px;
  border-radius: 10px;
  color: white;
  transition: all 0.3s;
}

.browse-button:hover {
  background-color: rgb(14, 14, 14);
}

.edit-details input[type="text"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  width: 50%;
  height: 40px;
}

.edit-details textarea {
  height: 140px;
  width: 50%;
  resize: vertical;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.edit-details input[type="text"]::placeholder,
.edit-details textarea::placeholder {
  color: #999;
}

.edit-details input[type="text"]:focus,
.edit-details textarea:focus {
  border-color: #3a6ea5;
  outline: none;
  box-shadow: 0 0 5px rgba(58, 110, 165, 0.5);
}

#submit-edit {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  border-radius: 10px;
  background: #3a6ea5;
  margin-bottom: 10px;
  color: white;
  border: none;
  cursor: pointer;
}

#submit-edit:hover {
  background: #002c58;
}
</style>
