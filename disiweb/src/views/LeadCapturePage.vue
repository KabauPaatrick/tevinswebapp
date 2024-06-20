<template>
    <div class="lead-capture">
        <h2>Contact Us!</h2>

        <form ref="form">
            <label for="phone_number">Phone Number</label>
            <label for="">Tel:0720964887</label>

            <label for="email">Email address</label>
            <input type=" email" id="email" name="email" placeholder="Enter your email address" />

            <button type="submit">{{ buttonText }}</button>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        buttonText: String,
    },
};
</script>

<style scoped>
.lead-capture {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 40px;
    min-height: 80vh;
    color: black;
    width: 700px;
    background: #cacbd5;
    box-shadow: rgb(31 38 135, 0.37 );
    border-radius: 10px;
}

.lead-capture h2 {
  font-size: 28px;
  margin-bottom: 20px;
}

/* Style for the form */
.lead-capture form {
  max-width: 400px;
  margin: 0 auto;
}

.lead-capture label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

.lead-capture input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.lead-capture button {
  background-color: orangered;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  width: 200px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Hover effect for the button */
.lead-capture button:hover {
  background-color: #007bff;
  transform: scale(1.05);
}

/* Responsive styling */
@media screen and (max-width: 600px) {
  .lead-capture input,
  .lead-capture button {
    width: 100%;
  }
}
</style>
