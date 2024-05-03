<template>
    <div class="container mt-5">
      <!-- License Form -->
      <div class="card mb-4">
        <div class="card-header">
          <h2 class="mb-0">Request For a Quotation</h2>
        </div>
        <div class="card-body">
          <form @submit.prevent="saveQuote" class="form">
            <div class="row">
              <div class="col-25">
                <label for="fname">First Name:</label>
              </div>
              <div class="col-75">
                <input type="text" id="fname" v-model="fname" class="form-control" placeholder="Enter Your First Name" required>
              </div>
            </div>
            <div class="row">
              <div class="col-25">
                <label for="lname">Last Name:</label>
              </div>
              <div class="col-75">
                <input type="text" id="lname" v-model="lname" class="form-control" placeholder="Enter Your Last Name" required>
              </div>
            </div>
            <div class="row">
              <div class="col-25">
                <label for="country">Country:</label>
              </div>
              <div class="col-75">
                <select id="country" v-model="country" class="form-control" required>
                  <option value="Kenya">Kenya</option>
                  <option value="Uganda">Uganda</option>
                  <option value="Tanzania">Tanzania</option>
                  <option value="Rwanda">Rwanda</option>
                </select>
              </div>
            </div>
            <div class="row">
              <div class="col-25">
                <label for="subject">Write your Enquiry:</label>
              </div>
              <div class="col-75">
                <textarea id="subject" v-model="quote" class="form-control" placeholder="Write something.." style="height:200px" required></textarea>
              </div>
            </div>
            <div class="row mt-3">
              <div class="col-md-12 d-flex justify-content-between">
                <button type="submit" class="btn btn-primary">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  <script>
  import axios from 'axios';
  export default{
    data() {
      return {
        api: 'http://127.0.0.1:8000/api/',
        fname: "",
        lname: "",
        phone: "",
        email: "",
        country: "",
        subject: "",
        quote: ""
      }
    },
    methods:{
      async saveQuote() {
  
  const formData ={
    fname: this.fname,
    lname: this.lname,
    phone: this.phone,
    email: this.email,
    country: this.country,
    subject: this.subject,
    quote: this.quote
  };
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/Clients/', formData);
  console.log(response.data);
     // Clear the form data after successful submission
  
  
  
  } catch (error) {
    console.error(error);             
    
  }
            this.fname = "";
            this.lname = "";
            this.phone = "";
            this.email = "";
            this.country = "";
            this.subject = "";
            this.quote = "";
  // const response = await axios.post('http://127.0.0.1:8000/api/Clients/', formData);
  // console.log(response.data);
  alert('Your submission has been submitted successfully!');
  }
    }
    
  
  
  
  
  }
  </script>
  <style>
  
  
  </style>