<template>
  <body>
    <div class="scroll">
      <div class="marque-yellow marque" v-show="currentMarque === 'yellow'">
        <div class="yellow-left">
          <img src="@/assets/images/girl.png" alt="" id="y-left">
        </div>
        <div class="yellow-right">
          <h1>Get the best deals!</h1>
          <h4>Up to 50% Off!</h4>
        </div>
      </div>
      <div class="marque-grey marque" v-show="currentMarque === 'grey'">
        <div class="g-left">
          <img src="@/assets/images/headphones.png" alt="" id="y-left">
        </div>
        <div class="g-right">
          <h1>High Quality!</h1>
          <h4>The best in the market</h4>
        </div>
      </div>
      <div class="marque-pink marque" v-show="currentMarque === 'pink'">
        <div class="pink-left">
          <img src="@/assets/images/sofa.png" alt="" id="p-left">
        </div>
        <div class="pink-right">
          <h1>Ultimate Home Makeover!</h1>
          <h4>Bring life to your home</h4>
        </div>
      </div>
    </div>
    <div class="nav-bar">
      <div class="dot" :class="{ active: currentMarque === 'yellow' }" @click="showMarque('yellow')"></div>
      <div class="dot" :class="{ active: currentMarque === 'grey' }" @click="showMarque('grey')"></div>
      <div class="dot" :class="{ active: currentMarque === 'pink' }" @click="showMarque('pink')"></div>
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
      </div>
      <div class="product1">
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
  data() {
    return {
      currentMarque: 'yellow',
      marqueOrder: ['yellow', 'grey', 'pink'],
      marqueIndex: 0,
      intervalId: null
    };
  },
  methods: {
    gotoproduct() {
      this.$router.push('/cart');
    },
    showMarque(marque) {
      this.currentMarque = marque;
      this.marqueIndex = this.marqueOrder.indexOf(marque);
    },
    nextMarque() {
      this.marqueIndex = (this.marqueIndex + 1) % this.marqueOrder.length;
      this.currentMarque = this.marqueOrder[this.marqueIndex];
    },
    startAutoSwitch() {
      this.intervalId = setInterval(this.nextMarque, 5000);
    },
    stopAutoSwitch() {
      clearInterval(this.intervalId);
    }
  },
  mounted() {
    this.startAutoSwitch();
  },
  beforeUnmount() {
    this.stopAutoSwitch();
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

.scroll {
  display: flex;
  flex-direction: column;
  overflow: hidden; /* Hide overflow to ensure items outside view */
}

.nav-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
  background: #cacbd5;
  width: 70px;
  height: 20px;
  border-radius: 10px;
}

.dot {
  width: 10px;
  height: 10px;
  background-color: white;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dot.active {
  background-color: #333;
}

.dot:hover {
  background-color: #333;
}

.marque {
  flex: 1;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  margin: 0 10px;
  display: none; /* Hide all marque elements by default */
}

.marque[v-show="true"] {
  display: flex; /* Show the current marque element */
}

.marque-content {
  display: flex;
  align-items: center;
}

.marque-left,
.marque-right {
  flex: 1;
  padding: 20px;
}

.marque-yellow {
  width: 90vw;
  height: 200px;
  background: linear-gradient(to right, #f6ea41, #f048c6);
  margin: 10px;
  justify-content: center;
  align-items: center;
  display: flex;
  border-radius: 10px;
}

.marque-grey {
  width: 90vw;
  height: 200px;
  background: linear-gradient(to right, #f3e9e8, #96b9d9);
  margin: 10px;
  overflow-x: hidden;
  justify-content: center;
  align-items: center;
  display: flex;
  border-radius: 10px;
}

.marque-pink {
  width: 90vw;
  height: 200px;
  background: linear-gradient(to right, #d09192, #c82471);
  margin: 10px;
  justify-content: center;
  align-items: center;
  display: flex;
  border-radius: 10px;
}

#y-left,
#g-left,
#p-left {
  max-height: 200px;
  max-width: 500px;
  display: block;
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
