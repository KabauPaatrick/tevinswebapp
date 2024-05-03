<template>
    <div class="container mt-5">
        <!-- Login Form -->
        <div class="card">
            <div class="card-header">
                <h2 class="mb-0">Login</h2>
            </div>
            <div class="card-body">
                <form @submit.prevent="login">
                    <!-- Username -->
                    <div class="form-group">
                        <label for="username">Username</label>
                        <input type="text" class="form-control" id="username" v-model="loginData.username"
                            placeholder="Enter username" required>
                    </div>
                    <!-- Password -->
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" class="form-control" id="password" v-model="loginData.password"
                            placeholder="Enter password" required>
                    </div>
                    <!-- Submit Button -->
                    <button type="submit" class="btn btn-primary">Login</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const loginData = reactive({
            username: '',
            password: ''
        });

        const login = async () => {
            try {
                const config = {
                    headers: {
                        'Content-Type': 'application/json',

                        'Authorization': `Bearer ${loginData.token}` // Include the authorization token
                    }
                };

                // Send login request to your backend API
                const response = await axios.post('http://edms-enpoints.bitz-itc.com/api/auth/login', loginData, config);

                // Store the token in local storage
                localStorage.setItem('edms_token', response.data.token);

                console.log(response.data);
                // Reset login form fields after successful login
                loginData.username = '';
                loginData.password = '';
                // Redirect user or perform other actions after successful login
            } catch (error) {
                console.error('Error logging in:', error);
                // Handle login error (e.g., display error message to the user)
            }
        };

        return {
            loginData,
            login
        };
    }
}
</script>

<style scoped>
/* Add custom styles here if needed */
.card {
    width: 300px;
    margin: auto;
    margin-top: 100px;
}
</style>
