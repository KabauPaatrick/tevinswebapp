<template>
  <div class="homepage">
    <NavBar />
    <HeroComp />
    <OurServicesComp />
    <TestimonialsComp />
    <ContactUsComp />
    
    <footer>
      <p>&copy; {{ year }} Byden Construction and Services</p>
    </footer>

    <div v-if="showChatWidget" id="tawkWidget"></div>
  </div>
</template>

<script>
import { ref } from 'vue';
import ContactUsComp from '@/components/ContactUsComp.vue';
import HeroComp from '@/components/HeroComp.vue';
import NavBar from '@/components/NavBar.vue';
import OurServicesComp from '@/components/OurServicesComp.vue';
import TestimonialsComp from '@/components/TestimonialsComp.vue';

export default {
  name: 'HomePage',
  components: {
    NavBar,
    HeroComp,
    OurServicesComp,
    TestimonialsComp,
    ContactUsComp
  },
  setup() {
    const year = ref(new Date().getFullYear());
    const showChatWidget = ref(false);

    const loadTawkToWidget = () => {
      if (typeof Tawk_API === "undefined") {
        const script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "https://embed.tawk.to/64ca9f36cc26a871b02cdf13/1h6rnrrt8";
        script.setAttribute("crossorigin", "*");
        document.body.appendChild(script);
        showChatWidget.value = true;
      }
    };

    loadTawkToWidget();

    return {
      year,
      showChatWidget,
    };
  }
};
</script>

<style scoped>
.homepage {
  overflow: hidden;
  background: #bdbdbf;
}

footer {
  text-align: center;
  padding: 20px;
  background: #1769FF;
  color: white;
}

#tawkWidget {
  position: fixed;
  bottom: 0;
  right: 0;
  z-index: 1000;
}
</style>