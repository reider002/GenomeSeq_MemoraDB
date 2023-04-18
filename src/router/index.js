import { createRouter, createWebHistory } from 'vue-router'
import GDCDashboard from '../views/Dashboard.vue'
import TestApiCalls from '../views/TestApiCalls.vue'
import AlleleData from '../views/AlleleData.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'gdcDashboard',
      component: GDCDashboard
    },
    {
      path: '/test-api-calls',
      name: 'testApiCalls',
      component: TestApiCalls
    },
    {
      path: '/allele-data',
      name: 'alleleData',
      component: AlleleData
    }
  ]
})

export default router
