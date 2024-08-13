<template>
  <body>
    <div class="cartitem">
      <div class="opt-images">
        <div class="img-box" @mouseover="displayImage(require(product.image), 0)">
          <img src="@/assets/images/picun-headphones.jpg" alt="" id="opt-img">
        </div>
        <div class="img-box" @mouseover="displayImage(require('@/assets/images/cones.jpg'), 1)">
          <img src="@/assets/images/cones.jpg" alt="" id="opt-img">
        </div>
        <div class="img-box" @mouseover="displayImage(require('@/assets/images/picun-battery.jpg'), 2)">
          <img src="@/assets/images/picun-battery.jpg" alt="" id="opt-img">
        </div>
        <div class="img-box" @mouseover="displayImage(require('@/assets/images/noise-cancel.jpg'), 3)">
          <img src="@/assets/images/noise-cancel.jpg" alt="" id="opt-img">
        </div>
        <div class="img-box" @mouseover="displayImage(require('@/assets/images/person-picun.jpg'), 4)">
          <img src="@/assets/images/person-picun.jpg" alt="" id="opt-img">
        </div>
        <div class="img-box" @mouseover="displayImage(require('@/assets/images/picun-final.jpg'), 5)">
          <img src="@/assets/images/picun-final.jpg" alt="" id="opt-img">
        </div>
        
      </div>

      <div class="cartitem-left">
        <img :src="product.image" alt="Cart Item Image" id="cartimage">
      </div>

      <div class="cartitem-right">
        <h4 id="title">{{product.title}}</h4>
        <div class="seller">
          <h5 id="seller-h5">Provided by |</h5>
          <img :src="product.image" alt="">
          <h5 id="seller">Seller 1</h5>
        </div>
        <div class="rating">
          <span 
            v-for="(rating, index) in product.ratings" 
            :key="index" 
            class="material-symbols-outlined star-icon">
            star
          </span>
        </div>
        <h5 id="price">ksh{{product.price}}</h5>
        <div class="count">
          <span class="material-symbols-outlined count-icon">hourglass_bottom</span>
          <h5 id="units">10 Units left</h5>
        </div>
        <div class="number">
          <h5 id="quantity">Quantity</h5>
          <input type="number" v-model="quantity" placeholder="1">
        </div>
        <button id="addtocart" @click="addToCart(product.id)"><span class="material-symbols-outlined cart-icon">shopping_cart</span>Add to Cart</button>
      </div>

      <div class="more-details">
        <h4 id="details-title">DELIVERY & RETURNS</h4>
        <hr class="solid">
        <h5>Choose Your Location</h5>
        <select name="locations" id="locations">
          <option value="Nairobi">Nairobi</option>
          <option value="Kisumu">Kisumu</option>
          <option value="Nakuru">Nakuru</option>
          <option value="Naivasha">Naivasha</option>
        </select>
        <div class="delivery">
          <div class="choice">
            <div class="coat"><span class="material-symbols-outlined delivery-icons">store</span></div>
            <h5 id="delivery-h5">Pickup Station</h5>
          </div>
          <div class="choice">
            <div class="coat"><span class="material-symbols-outlined delivery-icons">local_shipping</span></div>
            <h5 id="delivery-h5">Door Delivery</h5>
          </div>
          <div class="choice">
            <div class="coat"><span class="material-symbols-outlined delivery-icons">assignment_return</span></div>
            <h5 id="delivery-h5">Return Policy</h5>
          </div>
          <div class="choice">
            <div class="coat"><span class="material-symbols-outlined delivery-icons">security</span></div>
            <h5 id="delivery-h5">Warranty</h5>
          </div>
        </div>
      </div>
    </div>

    <div class="products-description">
      <h3 id="product-details">Product Details</h3>
      <hr class="solid">
      <ul id="prod-list">
        <li>JBL signature sound with PureBass performance and premium 50mm drivers deliver full spectrum sound with uninhibited clarity and powerful bass. Connectivity Technology: Wireless</li>
        <li>Bluetooth enabled technology for wireless calling and music play. Built-in Share Me technology allows you to share your content with another set of headphones, simultaneously</li>
        <li>Ear-cup-based microphone with echo-cancelation technology allows for hands-free calling with a pure connection to your wireless device for clear, hands free calling</li>
        <li>Built-in, USB rechargeable lithium-ion battery provides 16 hours of uninterrupted listening. And when the battery dies, the included aux cable allows for passive listening</li>
        <li>Ergonomic headband and protein leather ear-cushions provide an ultra-comfortable fit and effective noise isolation</li>
      </ul>
    </div>

    <div class="related">
      <h3>Customers also viewed</h3>
      <div class="products">
        <div class="product1">
          <img src="@/assets/images/pods.jpg" alt="" id="product-image">
          <h1>Soundcore Life Dot 2 XR True Wireless In-Ear Headphones - Gray (AKA3931ZA1-F0)</h1>
          <h5>$99.99</h5>
        </div>
        <div class="product1">
          <img src="@/assets/images/cones.jpg" alt="" id="product-image">
          <h1>Qc35 Replacement Ear Pads for Bose - QC35, QC45, QC35ii Replacement Earpads Cushion - Compatible with Quiet Comfort35, QC25, QC35ii, QC15, AE2, AE2i</h1>
          <h5>$127</h5>
        </div>
        <div class="product1">
          <img src="@/assets/images/watch.webp" alt="" id="product-image">
          <h1>Samsung Galaxy Watch4 Classic R880 42mm Black GPS + WiFi + Bluetooth - Very Good</h1>
          <h5>$46.99</h5>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CartItem',
  props: {
    msg: String
  },
  data() {
    return {
      product: {},
      quantity: 1
    };
  },
  mounted() {
    this.fetchProductDetails();
  },
  methods: {
    async fetchProductDetails() {
      const productId = this.$route.params.id;
      const productUrl = `https://kabau.pythonanywhere.com/api/products/${productId}/`;
      try {
        const response = await axios.get(productUrl);
        this.product = response.data;
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    },
    displayImage(image, index) {
      const cartImage = document.getElementById('cartimage');
      cartImage.src = image;

      const imgBoxes = document.querySelectorAll('.img-box');
      imgBoxes.forEach((box) => box.classList.remove('active'));

      imgBoxes[index].classList.add('active');
    },

    addtocart() {
      this.$router.push('/addtocart');
    },
  }
};
</script>

  
<style scoped>

body{
  display: grid;
  justify-content: center;
  align-items: center;
  
}

.opt-images{
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.img-box {
  height: 70px;
  width: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: 1px solid #DDDDDD;
  overflow: hidden;
  cursor: pointer;
}

.img-box.active{
  box-shadow: 0 0 5px rgba(81, 203, 238, 1);
  border: 1px solid rgba(81, 203, 238, 1);
}

#opt-img {
  max-width: 100%; 
  max-height: 100%;
  border-radius: 10px;
  object-fit: contain;
}

.cartitem {
  margin: auto;
  width: 90vw;
  display: flex;
  justify-content: space-between;
  padding: 50px;
  border-radius: 10px;
  color: black;
  gap: 10px;
}

.cartitem-left{
  max-width: 400px;
}

.cartitem-right{
  max-width: 300px;
}

#cartimage{
  max-width: 380px;
  max-height: 500px;
  border-radius: 0px;
  cursor: zoom-in;
  object-fit: contain;
}

#title{
  font-weight: 700;
}

#seller-h5{
  font-size: 15px;
  color: gray;
  font-weight: 400;
}

.seller{
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 7px 0;
}

.seller img{
  height: 20px;
  width: 20px;
  border-radius: 25px;
  cursor: pointer;
}

#seller{
  font-size: small;
  font-weight: 500;
  cursor: pointer;
}
#seller:hover{
  text-decoration: underline;
}

#price{
  font-size: 30px;
  font-weight: 400;
}

.count{
  align-items: center;
  display: flex;
}

.count-icon{
  color: #ff8500;
  font-size: 18px;
}

#units{
  font-size: 15px;
  color: #ff8500;
  font-weight: 400;
}

.star-icon {
  font-size: 18px;
  font-variation-settings:
    'FILL' 1,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24;
  color: #ff8500;
  cursor: pointer;
}

.number{
  display: flex;
  align-items: center;
  gap: 10px;
  border: solid 1px gray;
  padding: 10px;
  margin: 15px 0;
}

#quantity{
  font-size: 20px;
  font-weight: 400px;
}

.number input{
  height: 20px;
  width: 40px;
}

.cart-icon{
  margin-right: 10px;
}

button {
  display: flex; /* Enable flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  width: 210px;
  height: 50px;
  border-radius: 10px;
  background: #f2630d;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

button span:after {
  content: "»";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -15px;
  transition: 0.5s;
}

button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

button span:after {
  content: "»";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -15px;
  transition: 0.5s;
}

button:hover span {
  padding-right: 15px;
}

button:hover span:after {
  opacity: 1;
  right: 0;
}

button:hover{
  background: #3a6ea5;
}

#details-title{
  font-size: 15px;
  color: black;
}

.more-details{
  /* border: solid 1px grey; */
  background: #cacbd5;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  max-width: 300px;
}

hr.solid {
  border-top: 2px solid #323841;
  margin: 0;
}

#locations{
  width: 90%;
}

.more-details select{
  height: 40px;
  border-radius: 5px;
  padding: 5px;
  margin: 10px 0;
}

.choice{
  display: flex;
  
}

.delivery{
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.coat{
  padding: 5px;
  width: 35px;
  border: solid 1px grey;
  border-radius: 5px;
  margin-right: 10px;
}

.delivery-icons{
  font-variation-settings:
    'wght' 300;
}

#delivery-h5{
  font-weight: 500;
  font-size: 15px;
}

.products-description{
  width: 72%;
  background: #cacbd5;
  margin: 0 0 20px 0;
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

#product-details{
  margin: 0;
  color: black;
}

#prod-list{
  padding: 0;
  list-style: inside;
  margin: 0;
}

 /*================RELATED PRODUCTS CODE====================*/
.related{
  display: flex;
  flex-direction: column;
  padding: 10px;
  background: #cacbd5;
  border-radius: 10px;
  width: 72%;
  margin-bottom: 30px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.related h3{
  color: black;
}

.products {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  padding: 10px;
  gap: 10px;
  border-radius: 15px;
}

.product1 {
  background: #e9e9e9;
  height: 330px;
  width: 250px;
  padding: 10px;
  overflow: hidden;
  border-radius: 5px;
  color: black;
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* Adjust vertical spacing */
}

.product1 h1 {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* Number of lines to show */
  -webkit-box-orient: vertical;
  margin-bottom: 10px; /* Space between h1 and other elements */
}

.product1:hover{
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
}

.product1 h1 {
  font-size: large;
  margin-bottom: 0;
}

.product1 h5 {
  font-size: medium;
  margin: 0 0 20px 0;
}

#product-image {
  width: 100%;
  height: 200px;
}
</style>
  