<template>
    <div class="admin-products">
      <div class="products-body">
        <h1>YOUR PRODUCTS</h1>
        <hr class="solid">
  
        <div class="my-products">
          <div class="my-product1">
            <img src="@/assets/images/towelproduct.jpg" alt="" id="my-product-image">
            <h1>Utopia Towels 2 Pack Premium Bath Towels Set, (27 x 54 Inches) 100% Ring Spun Cotton 600GSM, Lightweight and Highly Absorbent Quick Drying Towels, Perfect for Daily Use</h1>
            <h5>$99.99</h5>
            <button id="edit" @click="editproduct"><span class="material-symbols-outlined edit-icon">edit</span>Edit</button>
            <button id="delete" @click="confirmDelete"><span class="material-symbols-outlined delete-icon">delete</span>Delete</button>
          </div>
          <div class="my-product1">
            <img src="@/assets/images/headphones.png" alt="" id="my-product-image">
            <h1>Item 1</h1>
            <h5>$100</h5>
            <button id="edit" @click="editproduct"><span class="material-symbols-outlined edit-icon">edit</span>Edit</button>
            <button id="delete" @click="confirmDelete"><span class="material-symbols-outlined delete-icon">delete</span>Delete</button>
          </div>
          <div class="my-product1">
            <img src="@/assets/images/towelproduct.jpg" alt="" id="my-product-image">
            <h1>Item 1</h1>
            <h5>$100</h5>
            <button id="edit" @click="editproduct"><span class="material-symbols-outlined edit-icon">edit</span>Edit</button>
            <button id="delete" @click="confirmDelete"><span class="material-symbols-outlined delete-icon">delete</span>Delete</button>
          </div>
        </div>
      </div>
  
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <h5>Are you sure you want to delete this item? The item will be permanently deleted.</h5>
          <div class="confirm-buttons">
              <button id="yes" @click="deleteItem">Yes</button>
              <button id="no" @click="cancelDelete">No</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'A-ProductsPage',
    data() {
      return {
        showPopup: false,
        itemToDelete: null
      };
    },
    methods: {
      editproduct() {
        this.$router.push('/editproductpage');
      },
      confirmDelete(item) {
        this.showPopup = true;
        this.itemToDelete = item;
      },
      deleteItem() {
        // Perform delete action here
        this.showPopup = false;
        this.itemToDelete = null;
      },
      cancelDelete() {
        this.showPopup = false;
        this.itemToDelete = null;
      }
    }
  };
  </script>
  
  <style scoped>
  .admin-products {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 30px 0 20px 50px;
  }
  
  .products-body{
    display: flex;
    flex-direction: column;
    width: 90%;
    background: #cacbd5;
    padding: 10px;
    border-radius: 10px;
    color: black;
  }
  
  .products-body h1{
    font-size: 25px;
    margin: 0;
  }
  
  .my-products {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    padding: 10px;
    margin-bottom: 30px;
    gap: 10px;
    border-radius: 15px;
    padding-left: 80px;
  }
  
  .my-product1 {
    width: 250px;
    background: #e9e9e9;
    padding: 10px;
    overflow: hidden;
    border-radius: 5px;
    color: black;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* Adjust vertical spacing */
  }
  
  .my-product1 h1 {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2; /* Number of lines to show */
    -webkit-box-orient: vertical;
    margin-bottom: 10px; /* Space between h1 and other elements */
  }
  
  .my-product1:hover{
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
  }
  
  .my-product1 h1 {
    font-size: large;
  }
  
  .my-product1 h5 {
    font-size: medium;
  }
  
  #my-product-image {
    width: 100%;
    height: 200px;
  }
  
  #edit {
    display: flex; /* Enable flexbox */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    width: 100%;
    height: 50px;
    border-radius: 10px;
    background: #3a6ea5;
    margin-bottom: 10px;
  }
  #edit:hover{
    background: #002c58;
  }
  
  #delete {
    display: flex; /* Enable flexbox */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    width: 100%;
    height: 50px;
    border-radius: 10px;
    background: #e4000f;
    margin-bottom: 10px;
  }
  
  #delete:hover{
    background: #740001;
  }
  
  .popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    z-index: 1000;
  }

  .confirm-buttons{
    display: flex;
  }

  #yes{
    display: flex; /* Enable flexbox */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 50px;
    border-radius: 10px;
    background: #e4000f;
    margin-bottom: 10px;
  }
  
  #no{
    display: flex; /* Enable flexbox */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 50px;
    border-radius: 10px;
    background: #3a6ea5;
    margin-bottom: 10px;
  }

  .popup-content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .popup-content p {
    margin-bottom: 20px;
  }
  
  .popup-content button {
    margin: 5px;
  }
  </style>
  