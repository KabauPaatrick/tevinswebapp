<template>
    <div class="card-container">
      <div class="circle1"></div>
      <div class="circle2"></div>
      <div class="container">
        <div class="signup-card">
          <p class="heading">Welcome!</p>
          <p>We are happy to have you</p>
          <form>
            <div class="input-group">
              <p class="text">Username</p>
              <input class="input" type="text" placeholder="Enter Username" required>
              <p class="text">Email</p>
              <input class="input" type="email" placeholder="Enter Email" required>
              <p class="text">Telephone</p>
              <input class="input" type="tel" placeholder="07xxxxxxxx" required>
              <p class="text">Password</p>
              <input class="input" type="password" placeholder="Enter Password" required>
            </div>
            <button type="submit" class="btn">Sign Up</button>
          </form>
          <p class="no-account">Already Have an Account?<router-link to="/login" class="link"> Log in</router-link></p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SignupPage',
    props: {
      msg: String
    },
  }
  </script>
  
  <style scoped>
  .card-container {
    width: 350px;
    height: 540px;
    background: transparent;
    position: relative;
    margin: auto;
    top: 100px;
  }
  
  .container {
    display: flex;
    height: 100%;
    width: 100%;
    align-items: center;
    justify-content: center;
  }
  
  .circle1 {
    height: 80px;
    width: 80px;
    border-radius: 50%;
    background-color: #2879f3;
    position: absolute;
    top: 0;
    left: 0;
  }
  
  .circle2 {
    height: 80px;
    width: 80px;
    border-radius: 50%;
    background-color: #f37e10;
    position: absolute;
    right: 0;
    bottom: 0;
  }
  
  .signup-card {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    position: absolute;
    width: 300px;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(5px);
    padding: 20px;
  }
  
  .heading {
    font-size: 28px;
    font-weight: 800;
  }
  
  .text {
    margin-top: 5px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: 600;
    color: lightslategray;
  }
  
  .input-group {
    margin-top: 10px;
    margin-bottom: 4px;
  }
  
  .input {
    box-sizing: border-box;
    margin-bottom: 5px;
    width: 100%;
    border: none;
    padding: 8px 16px;
    background-color: transparent;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
    border-radius: 8px;
    font-weight: 600;
    color: black;
  }
  
  .input:hover {
    color: #2879f3;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
  }
  
  .btn {
    margin-top: 20px;
    margin-bottom: 10px;
    padding: 8px 16px;
    border: none;
    background-color: #2879f3;
    color: white;
    font-size: 16px;
    font-weight: 700;
    border-radius: 8px;
  }
  
  .btn:hover {
    background-color: #0653c7;
  }
  
  .link {
    font-weight: 800;
    color: #2879f3;
  }
  
  .link:hover {
    color: red;
    text-decoration: underline;
  }
  </style>
  