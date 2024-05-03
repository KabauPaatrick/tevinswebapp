<template>
    <div class="container mt-5">
        <!-- Customer Form -->
        <div class="card mb-4">
            <div class="card-header">
                <h2 class="mb-0">Customer Information</h2>
            </div>
            <div class="card-body">
                <form @submit.prevent="submitCustomer">
                    <div class="row">
                        <div class="col-md-6">
                            <!-- Name -->
                            <div class="form-group">
                                <label for="name">Name</label>
                                <input type="text" class="form-control" id="name" v-model="customer.name"
                                    placeholder="Enter customer name" required>
                            </div>
                            <!-- Email -->
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" class="form-control" id="email" v-model="customer.email"
                                    placeholder="Enter email" required>
                            </div>
                            <!-- Phone Number -->
                            <div class="form-group">
                                <label for="phone_number">Phone Number</label>
                                <input type="tel" class="form-control" id="phone_number" v-model="customer.phone_number"
                                    placeholder="Enter phone number" required>
                            </div>
                            <!-- Address -->
                            <div class="form-group">
                                <label for="address">Address</label>
                                <input type="text" class="form-control" id="address" v-model="customer.address"
                                    placeholder="Enter address" required>
                            </div>

                        </div>
                        <div class="col-md-6">
                            <!-- City -->
                            <div class="form-group">
                                <label for="city">City</label>
                                <input type="text" class="form-control" id="city" v-model="customer.city"
                                    placeholder="Enter city" required>
                            </div>
                            <!-- State -->
                            <div class="form-group">
                                <label for="state">State</label>
                                <input type="text" class="form-control" id="state" v-model="customer.state"
                                    placeholder="Enter state" required>
                            </div>
                            <!-- Country -->
                            <div class="form-group">
                                <label for="country">Country</label>
                                <input type="text" class="form-control" id="country" v-model="customer.country"
                                    placeholder="Enter country" required>
                            </div>
                            <!-- Postal Code -->
                            <div class="form-group">
                                <label for="postal_code">Postal Code</label>
                                <input type="text" class="form-control" id="postal_code" v-model="customer.postal_code"
                                    placeholder="Enter postal code" required>
                            </div>
                            <!-- Created By -->
                            <div class="form-group">
                                <label for="createdBy">Created By</label>
                                <input type="text" class="form-control" id="createdBy" v-model="customer.created_by"
                                    placeholder="Enter creator name" required>
                            </div>
                        </div>
                    </div>
                    <!-- Created At and Updated At -->
                    <div class="row">
                        <div class="col-md-6">
                            <!-- Created At -->
                            <div class="form-group">
                                <label for="createdAt">Created At</label>
                                <input type="datetime-local" class="form-control" id="createdAt"
                                    v-model="customer.createdAt" required>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <!-- Updated At -->
                            <div class="form-group">
                                <label for="updatedAt">Updated At</label>
                                <input type="datetime-local" class="form-control" id="updatedAt"
                                    v-model="customer.updatedAt" required>
                            </div>
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col-md-6">
                            <!-- Submit Button -->
                            <button type="submit" class="btn btn-primary">Create</button>
                        </div>
                        <div class="col-md-6">
                            <!-- Update Button -->
                            <button type="button" class="btn btn-primary"
    @click="updateCustomerOnSubmit(customer.id)">Save-Update</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

        <!-- Customer Table -->
        <div class="card">
            <div class="card-header">
                <h2 class="mb-0">Customer List</h2>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Phone Number</th>
                                <th>Address</th>
                                <th>City</th>
                                <th>State</th>
                                <th>Country</th>
                                <th>Postal Code</th>
                                <th>Created By</th>
                                <th>Created At</th>
                                <th>Updated At</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(customer, index) in customers" :key="index">
                                <td>{{ customer.name }}</td>
                                <td>{{ customer.email }}</td>
                                <td>{{ customer.phone_number }}</td>
                                <td>{{ customer.address }}</td>
                                <td>{{ customer.city }}</td>
                                <td>{{ customer.state }}</td>
                                <td>{{ customer.country }}</td>
                                <td>{{ customer.postal_code }}</td>
                                <td>{{ customer.created_by }}</td>
                                <td>{{ customer.createdAt }}</td>
                                <td>{{ customer.updatedAt }}</td>
                                <td>
                                    <button @click="deleteCustomer(customer.id)" class="btn btn-danger">Delete</button>
                                    <button @click="updateCustomerForm(customer)"
                                        class="btn btn-primary">Update</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive, onMounted } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const customer = reactive({
            name: '',
            email: '',
            phone_number: '',
            address: '',
            city: '',
            state: '',
            country: '',
            postal_code: '',
            created_by: '',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        });

        const customers = reactive([]);

        const fetchCustomers = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/customer/show/');
                customers.splice(0, customers.length, ...response.data);
            } catch (error) {
                console.error('Error fetching customers:', error);
            }
        };

        const submitCustomer = async () => {
            try {
                customer.createdAt = customer.createdAt.toString();
                customer.updatedAt = customer.updatedAt.toString();
                const response = await axios.post('http://127.0.0.1:8000/api/customer/create/', customer);
                console.log(response.data);
                Object.keys(customer).forEach(key => {
                    customer[key] = '';
                });
                await fetchCustomers();
            } catch (error) {
                console.error('Error submitting customer:', error);
            }
        };

        const deleteCustomer = async (customerId) => {
            try {
                const response = await axios.delete(`http://127.0.0.1:8000/api/customer/${customerId}/delete`);
                console.log(response.data);
                await fetchCustomers();
            } catch (error) {
                console.error('Error deleting customer:', error);
            }
        };

        const updateCustomerForm = (customerData) => {
            customer.name = customerData.name;
            customer.email = customerData.email;
            customer.phone_number = customerData.phone_number;
            customer.address = customerData.address;
            customer.city = customerData.city;
            customer.state = customerData.state;
            customer.country = customerData.country;
            customer.postal_code = customerData.postal_code;
            customer.created_by = customerData.created_by;
            customer.createdAt = customerData.createdAt || new Date().toISOString(); // Initialize if not provided
            customer.updatedAt = new Date().toISOString(); // Update the updatedAt field
        };

        const updateCustomerOnSubmit = async (customerId) => {
            try {
                const response = await axios.put(`http://127.0.0.1:8000/api/customer/${customerId}/update/`, customer);
                console.log(response.data);
                Object.keys(customer).forEach(key => {
                    customer[key] = '';
                });
                await fetchCustomers();
            } catch (error) {
                console.error('Error updating customer:', error);
            }
        };


        onMounted(() => {
            fetchCustomers();
        });

        return {
            customer,
            customers,
            submitCustomer,
            deleteCustomer,
            updateCustomerForm,
            updateCustomerOnSubmit
        };
    }
}
</script>

<style scoped>
/* Add custom styles here if needed */
.card {
    margin-bottom: 20px;
}
</style>
