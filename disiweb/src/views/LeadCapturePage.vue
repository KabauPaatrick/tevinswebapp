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

</style>
