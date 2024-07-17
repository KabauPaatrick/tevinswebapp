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
                  <input id="file" type="file" />
                </label>
              </form>
              <form class="edit-details">
                <input type="text" placeholder="Product Name">
                <input type="text" placeholder="Enter Price">
                <textarea name="Prod-details" id="Prod-details" placeholder="Enter Product Details"></textarea>
                <button id="submit-edit">Submit</button>
              </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'EditProduct',
  props: {
    msg: String
  },
}
</script>

<style scoped>
.edit-body{
  background: #cacbd5;
  display: flex;
  flex-direction: column;
  margin: auto;
  margin-top: 30px;
  width: 70vw;
  border-radius: 10px;
  padding: 10px;
}

h1{
  font-size: 30px;
  margin-bottom: 0;
  color: black;
}

.edit-product{
  display: flex;
  flex-direction: column;
}

.edit-data{
  display: flex;
  gap: 30px;
}

.edit-details{
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

.upload-icon{
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

.edit-details input[type="text"]{
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
  resize: vertical; /* Allow vertical resizing */
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
  border-color: #3a6ea5; /* Change border color on focus */
  outline: none; /* Remove default outline */
  box-shadow: 0 0 5px rgba(58, 110, 165, 0.5); /* Add subtle box shadow on focus */
}

#submit-edit{
  display: flex; /* Enable flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 50px;
  border-radius: 10px;
  background: #3a6ea5;
  margin-bottom: 10px;
}

#submit-edit:hover{
  background: #002c58;
}

</style>