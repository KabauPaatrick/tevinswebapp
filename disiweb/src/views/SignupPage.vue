<template>
  <div class="card-container">
    <div class="circle1"></div>
    <div class="circle2"></div>
    <div class="container">
      <div class="signup-card">
        <p class="heading">Welcome!</p>
        <p>We are happy to have you</p>
        <form @submit.prevent="register">
          <div class="input-group">
            <p class="text">Firstname</p>
            <input class="input" type="text" v-model="userData.first_name" placeholder="Enter Firstname" required>
            <p class="text">Lastname</p>
            <input class="input" type="text" v-model="userData.last_name" placeholder="Enter Lastname" required>
            <p class="text">Username</p>
            <input class="input" type="text" v-model="userData.username" placeholder="Enter Username" required>
            <p class="text">Email</p>
            <input class="input" type="email" v-model="userData.email" placeholder="Enter Email" required>
            <p class="text">Telephone</p>
            <input class="input" type="tel" v-model="userData.phone_number" placeholder="07xxxxxxxx" required>
            <p class="text">Password</p>
            <input class="input" type="password" v-model="userData.password" placeholder="Enter Password" required>
          </div>
          <button type="submit" class="btn">Sign Up</button>
        </form>
        <p class="no-account">Already Have an Account? <router-link to="/login" class="link">Log in</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
// import { useRouter } from 'vue-router';

export default {
  name: 'SignupPage',
  setup() {
    const userData = reactive({
      first_name:'',
      last_name:'',
      username: '',
      email: '',
      phone_number: '',
      password: '',
    });

    // const router = useRouter();

    const register = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/create/', userData);

        console.log('Successful Registration', response.data);

        // Clear form fields after successful registration
        userData.first_name='';
        userData.last_name='';
        userData.username = '';
        userData.email = '';
        userData.phone_number = '';
        userData.password = '';

        // Handle the response data as needed, e.g., storing user info or redirecting
        // Example: store user data in local storage
        localStorage.setItem('user', JSON.stringify(response.data));

        // Redirect to a different page after registration
        // router.push({ name: 'somePage' });
      } catch (error) {
        console.error('Error registering:', error);
      }
    };

    return {
      userData,
      register
    };
  }
}
</script>

<style scoped>
.card-container {
  width: 100%;
  max-width: 700px;
  height: 100vh;
  background: transparent;
  position: relative;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: center;
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
  width: 100%;
  max-width: 500px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(5px);
  padding: 30px;
  background-color: white;
}

.heading {
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 20px;
}

.text {
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 16px;
  font-weight: 600;
  color: lightslategray;
}

.input-group {
  margin-top: 20px;
  margin-bottom: 20px;
}

.input {
  box-sizing: border-box;
  margin-bottom: 15px;
  width: 100%;
  border: none;
  padding: 12px 20px;
  background-color: #f0f0f0;
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
  padding: 12px 20px;
  border: none;
  background-color: #2879f3;
  color: white;
  font-size: 18px;
  font-weight: 700;
  border-radius: 8px;
  width: 100%;
  max-width: 300px;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.btn:hover {
  background-color: #0653c7;
  transform: scale(1.05);
}

.no-account {
  margin-top: 20px;
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
