<template>
    <div>
    <AdminNav />
    <Admintop />
    <div class="container mt-5"></div>
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
import AdminNav from '@/components/AdminNav.vue';
import Admintop from '@/components/Admintop.vue';

export default {
    components: {
    AdminNav,
    Admintop
  },
    setup() {
        const formatDate = (dateString) => {
            return new Date(dateString).toISOString().slice(0, 16); // Format the date string
        };
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
            createdAt: formatDate(new Date()), // Initialize createdAt with current date
            updatedAt: formatDate(new Date())
        });

        const customers = reactive([]);

        const fetchCustomers = async () => {
            try {
                const response = await axios.get('https://kabau.pythonanywhere.com/api/customer/show/');
                customers.splice(0, customers.length, ...response.data);
            } catch (error) {
                console.error('Error fetching customers:', error);
            }
        };

        const submitCustomer = async () => {
            try {
                customer.createdAt = customer.createdAt.toString();
                customer.updatedAt = customer.updatedAt.toString();
                const response = await axios.post('https://kabau.pythonanywhere.com/api/customer/create/', customer);
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
                const response = await axios.delete(`https://kabau.pythonanywhere.com/api/customer/${customerId}/delete`);
                console.log(response.data);
                await fetchCustomers();
            } catch (error) {
                console.error('Error deleting customer:', error);
            }
        };

        const updateCustomerForm = (customerData) => {
            customer.id = customerData.id;
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


        const updateCustomerOnSubmit = async () => {
            try {
                if (!customer.id) {
                    console.error('Customer ID is undefined');
                    return;
                }
                const response = await axios.put(`https://kabau.pythonanywhere.com/api/customer/${customer.id}/update/`, customer);
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
    margin-left: 80px;
}
</style>