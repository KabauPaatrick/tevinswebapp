<template>
  <div class="card-container">
    <div class="circle1"></div>
    <div class="circle2"></div>
    <div class="container">
      <div class="signup-card">
        <p class="heading">Request For a Quotation</p>
        <form @submit.prevent="saveQuote" class="form">
          <div class="input-group">
            <label for="fname" class="text">First Name:</label>
            <input type="text" id="fname" v-model="fname" class="input" placeholder="Enter Your First Name" required>

            <label for="lname" class="text">Last Name:</label>
            <input type="text" id="lname" v-model="lname" class="input" placeholder="Enter Your Last Name" required>

            <label for="country" class="text">Country:</label>
            <select id="country" v-model="country" class="input" required>
              <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
            </select>

            <label for="subject" class="text">Write your Enquiry:</label>
            <textarea id="subject" v-model="quote" class="input" placeholder="Write something..." style="height:250px" required></textarea>
          </div>
          <button type="submit" class="btn">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      api: 'https://kabau.pythonanywhere.com/',
      fname: "",
      lname: "",
      phone: "",
      email: "",
      country: "",
      subject: "",
      quote: "",
      countries: [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
        "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
        "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
        "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
        "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
        "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
        "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
        "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
        "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
        "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
        "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
        "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
        "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
        "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
        "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
        "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain",
        "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
        "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
        "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
      ]
    }
  },
  methods: {
    async saveQuote() {
      const formData = {
        fname: this.fname,
        lname: this.lname,
        phone: this.phone,
        email: this.email,
        country: this.country,
        subject: this.subject,
        quote: this.quote
      };

      try {
        const response = await axios.post('https://kabau.pythonanywhere.com/api/Clients/', formData);
        console.log(response.data);

        // Clear the form data after successful submission
        this.fname = "";
        this.lname = "";
        this.phone = "";
        this.email = "";
        this.country = "";
        this.subject = "";
        this.quote = "";

        alert('Your submission has been submitted successfully!');
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>

<style scoped>
.card-container {
  width: 100%;
  height: 100vh;
  background: transparent;
  position: relative;
  display: flex;
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
  font-size: 28px;
  font-weight: 800;
  margin-bottom: 20px;
}

.text {
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 14px;
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
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
}

.btn {
  width: 100%;
  padding: 15px 20px;
  background-color: #2879f3;
  border-radius: 8px;
  color: white;
  font-size: 18px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.btn:hover {
  background-color: #0056b3;
}
</style>
