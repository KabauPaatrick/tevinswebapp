<template>
    <div class="cart-body">
        <div class="addcart">
            <h2>Cart</h2>
            <hr class="solid">
            <div class="items">
                <div class="items-img">
                    <img src="@/assets/images/picun-headphones.jpg" alt="" id="add-img">
                </div>
                <div class="item-details">
                    <h4>Picun Wireless Headphones, 120 Hours Headphones Wireless, Hands-Free Calls, 3EQ &Game Mode, Foldable Headphones Over Ear For Travel Home Office Cellphone PC</h4>
                    <h5 id="seller-id">Seller: Patrick Kabau</h5>
                    <div class="number">
                        <span class="material-symbols-outlined error">error</span><h5>8 units left</h5>
                    </div>
                </div>
                <div class="price">
                    <h2>Ksh 2,500</h2>
                </div>
            </div>
            <div class="add-item">
                <div class="add-right">
                    <button id="remove" @click="confirmRemove"><span class="material-symbols-outlined remove-icon">delete</span>Remove</button>
                </div>
                <div class="add-left">
                    <button id="minus">-</button>
                    <h4>1</h4>
                    <button id="plus">+</button>
                </div>
            </div>
        </div>
        <div class="summary">
            <h2>CART SUMMARY</h2>
            <hr class="solid">
            <div class="info">
                <h3>Subtotal</h3>
                <h2>Ksh 2,500</h2>
            </div>
            <h5>Delivery fees not included yet</h5>
            <button id="checkout">Proceed to Checkout (1 item)</button>
        </div>

        <div v-if="showPopup" class="popup">
            <div class="popup-content">
                <h5>Are you sure you want to remove this item from our cart?</h5>
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
    name: 'AddtoCart',
    data() {
      return {
        showPopup: false,
        itemToDelete: null
      };
    },
    methods: {
      confirmRemove(item) {
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
.cart-body{
    display: flex;
    padding: 50px;
    gap: 20px;
    width: 90vw;
    color: black;
}

h2{
    margin-bottom: 0;
}

.addcart{
    display: flex;
    flex-direction: column;
    margin: auto;
    width: 70vw;
    background: #cacbd5;
    padding: 10px;
    border-radius: 10px;
}

#add-img{
    max-width: 100%; 
    max-height: 100%;
    object-fit: contain;
}

.items-img{
    max-width: 100px;
}

.items{
    display: flex;
    gap: 10px;
}

h4{
    font-weight: 400;
    font-size: 20px;
}

h5{
    font-weight: 400;
    font-size: 15px;
}

.item-details{
    width: 60%;
}

.number{
    display: flex;
    gap: 2px;
    cursor: pointer;
    color: red;
    
}

.error{
    font-size: 19px;
    font-variation-settings:
    'FILL' 0,
    'wght' 300,
    'GRAD' 0,
    'opsz' 24;
    color: red;
}

.price{
    margin-left: auto;
}

.add-item{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}

.add-right{
    display: flex;
    padding: 5px;
    width: 120px;
    height: 35px;
    border-radius: 10px;
    color: red;
    cursor: pointer;
}

#remove {
    display: flex; /* Enable flexbox */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    width: 100%;
    height: 40px;
    border-radius: 10px;
    background: #e4000f;
    margin-bottom: 10px;
  }
  
#remove:hover{
    background: #740001;
}

.add-left{
    display: flex;
    align-items: center;
    gap: 10px;
}

#minus{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 30px;
    border-radius: 5px;
    font-size: 30px;
    padding-bottom: 20px;
}

#plus{
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50px;
    height: 30px;
    border-radius: 5px;
    font-size: 30px;
    padding-bottom: 20px;
}

button:hover{
    background: #c65314;
}

.summary{
    background: #cacbd5;
    padding: 10px;
    border-radius: 10px;
    width: 300px;
    height: 220px;
}

.summary h2{
    font-size: 18px;
    color: black;
}

.info{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
}

.info h3{
    font-size: 18px;
    color: rgb(69, 65, 65);
}

.info h2{
    font-size: 24px; 
}

.summary h5{
    font-size: 15px; 
    color: rgb(69, 65, 65);
}

#checkout{
    margin: 10px 0;
    border-radius: 5px;
    width: 100%;
    font-size: 17px;
    font-weight: 500;
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