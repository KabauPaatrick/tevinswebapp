import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "./assets/Styles/style.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import '@coreui/coreui/dist/css/coreui.min.css'
import axios from "axios";
const app = createApp(App);
const hostname = window.location.hostname;
if (hostname === "edms.bitz-itc.com") {
    // if (hostname === "localhost") {
    app.config.globalProperties.baseApiUrl =
        "http://edms-enpoints.bitz-itc.com";
    app.config.globalProperties.apiBaseUrl =
        "http://edms-enpoints.bitz-itc.com/api";
    axios.defaults.baseURL = "http://edms-enpoints.bitz-itc.com/api";
} else {
    console.log(hostname);
    app.config.globalProperties.baseApiUrl = "http://127.0.0.1:8000";
    app.config.globalProperties.apiBaseUrl = "http://127.0.0.1:8000/api";
    axios.defaults.baseURL = "http://127.0.0.1:8000/api";
}


createApp(App).use(router).mount('#app')
