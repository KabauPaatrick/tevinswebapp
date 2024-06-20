<template>
    <body>
        <div class="image">
            <img src="@/assets/images/Order Confirmed 1.png" alt="Cart Item Image" id="headimage">
        </div>
        <div class="products">
            <div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div>
            <div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div><div class="product1">
                <img src="@/assets/images/towelproduct.jpg" alt="" id="product-image">
                <h1>Item 1</h1>
                <h5>$100</h5>
                <button id="go" @click="gotoproduct">View Item</button>
            </div>
        </div>
    </body>
  </template>
  
  <script>
  export default {
    name: 'ProductsPage',
    props: {
      msg: String
    },
    methods:{
    gotoproduct() {
        this.$router.push('/cart');
    }
    }
  };
  </script>
  
  <style scoped>
body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#headimage {
  width: 200px;
}

.products {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  width: 98%;
  padding: 10px;
  margin-bottom: 30px;
  gap: 20px;
  border-radius: 15px;
  padding-left: 80px;
}

.product1 {
  height: 320px;
  width: 250px;
  background: #cacbd5;
  padding: 20px;
  overflow: hidden;
  border-radius: 15px;
  color: black;
}

.product1 h1 {
  font-size: large;
}

.product1 h5 {
  font-size: medium;
}

#product-image {
  width: 210px;
  height: 170px;
}

#go {
  display: flex; /* Enable flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  width: 210px;
  height: 50px;
  border-radius: 10px;
  background: #f2630d;
}

</style>