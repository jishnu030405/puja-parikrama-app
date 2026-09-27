import { createApp } from 'vue'
import { inject } from '@vercel/analytics'
import './assets/styles/main.css'
import App from './App.vue'
inject()

createApp(App).mount('#app')
