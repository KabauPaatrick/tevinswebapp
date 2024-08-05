<template>
  <section class="contact">
    <div class="Box">
      <aside class="contact__aside">
        <div class="aside__image">
          <img src="@/assets/images/talking.gif" alt="" id="lead-image">
        </div>
        <h2>Contact Us</h2>
        <p>Do you have any questions or issues you'd like to address? Contact Us through the given details:</p>
        <label for="">Tel:0720964887</label>
      </aside>
      <form ref="form" class="contact__form">
        <div class="form-data">
          <input type="email" id="email" name="email" placeholder="Enter email">
        </div>
        <router-link to="/contact">
          <button type="submit">{{ buttonText }}</button>
        </router-link>
      </form>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    buttonText: String,
  },
};
</script>

<style scoped>
.contact {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.Box {
  background: rgba(106, 188, 226, 0.25);
  box-shadow: rgb(31 38 135, 0.37);
  backdrop-filter: blur(0px);
  padding: 4rem;
  display: grid;
  grid-template-columns: 40% 40% 20%;
  gap: 4rem;
  height: 30rem;
  border-radius: 1rem;
  width: 800px;
}

.contact__aside {
  background: #007bff;
  padding: 3rem;
  border-radius: 1rem;
  position: relative;
  bottom: 10rem;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  color: white;
}

#lead-image{
  width: 200px;
}

.contact__aside h2 {
  text-align: left;
  margin-bottom: 1rem;
}

.contact__aside p {
  font-size: 0.9rem;
  margin-bottom: 2rem;
}

.contact__form {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin-right: 4rem;
}

.contact__form input[type="email"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.contact__form button {
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

.contact__form button:hover {
  background-color: #007bff;
  transform: scale(1.05);
}

@media screen and (max-width: 600px) {
  .contact__aside{
    background: #007bff;
    padding: 3rem;
    border-radius: 1rem;
    position: relative;
    bottom: 10rem;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    color: white;
  }

  .contact__form input[type="email"],
  .contact__form button {
    width: 100%;
  }
}
</style>
