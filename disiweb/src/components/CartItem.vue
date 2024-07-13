<template>
  <body>
    <div class="cartitem">
      <div class="cartitem-left">
        <img src="@/assets/images/TUK.jpg" alt="Cart Item Image" id="cartimage">
      </div>
      <div class="cartitem-right">
        <h1>Item 1</h1>
        <h5 id="seller">Seller 1</h5>
        <h5>$100</h5>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis voluptatem nisi vitae, repellendus cumque eveniet voluptatum sint impedit architecto quis.</p>
        <button id="addtocart">Add to Cart</button>
      </div>
    </div>
  </body>
</template>
  
  <script>
  export default {
    name: 'CartItem',
    props: {
      msg: String
    }
  };
  </script>
  
  <style scoped>

  .cartitem {
    margin: 20px 100px 30px 200px;
    width: 80vw;
    display: grid;
    grid-template-columns: auto 1fr;
    background: #cacbd5;
    padding: 50px;
    border-radius: 10px;
    color: black;
  }

  img{
    width: 90%;
    height: auto;
    border-radius: 0px;
  }

  #seller{
    font-size: small;
  }

  button {
  display: flex; /* Enable flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  width: 210px;
  height: 50px;
  border-radius: 10px;
  background: #f2630d;
}

  button:hover{
    background: #3a6ea5;
  }
  </style>
  