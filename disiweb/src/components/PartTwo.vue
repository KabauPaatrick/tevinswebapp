<template>
    <div class="landing-page">
      <header>
        <slot name="logo"></slot>
        <NavBar />
      </header>
  
      <main>
        <div>
          <Hero v-if="heroContent" :content="heroContent" />
        </div>
  
        <div>
          <Benefits />
        </div>
  
        <div>
          <OurAchievements />
        </div>
  
        <div>
          <LicenseViewVue />
        </div>
  
        <div>
          <Testimonials v-if="testimonialsList" :list="testimonialsList" />
        </div>
  
        <div>
          <LeadCapture v-if="leadCaptureForm" :buttonText="leadCaptureButtonText" />
        </div>
      </main>
  
      <footer>
        <p>&copy; {{ year }} Your Company Name</p>
      </footer>
  
      <div v-if="showChatWidget" id="tawkWidget"></div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import Hero from '@/views/HeroPage.vue';
  import Benefits from '@/views/BenefitsPage.vue';
  import Testimonials from '@/views/TestimonialsPage.vue';
  import LeadCapture from '@/views/LeadCapturePage.vue';
  import NavBar from '@/components/NavBar.vue';
//   import OurAchievements from './OurAchievements.vue';
//   import LicenseViewVue from './LicenseView.vue';
  
  export default {
    components: {
      Hero,
      Benefits,
      Testimonials,
      LeadCapture,
      NavBar,
    //   OurAchievements,
    //   LicenseViewVue,
    },
    setup() {
      const heroContent = ref({
        title: "Your Company Name",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        ctaText: "Learn more",
        imageUrl: require("../assets/images/HeroImage.png"),
      });
      const testimonialsList = ref([
        { name: "Testimonial 1", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." },
        { name: "Testimonial 2", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." },
      ]);
      const leadCaptureForm = ref("Lead Capture");
      const leadCaptureButtonText = ref("Learn from us");
      const year = ref(new Date().getFullYear());
      const showChatWidget = ref(false);
  
      const setHeroContent = (content) => {
        heroContent.value = content;
      };
  
      const setTestimonialsList = (list) => {
        testimonialsList.value = list;
      };
  
      const setLeadCaptureForm = (form, buttonText) => {
        leadCaptureForm.value = form;
        leadCaptureButtonText.value = buttonText;
      };
  
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
        heroContent,
        testimonialsList,
        leadCaptureForm,
        leadCaptureButtonText,
        year,
        setHeroContent,
        setTestimonialsList,
        setLeadCaptureForm,
        showChatWidget,
      };
    },
  };
  </script>
  