import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import TestApiCalls from '../views/TestApiCalls.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/test-api-calls',
      name: 'testApiCalls',
      component: TestApiCalls
    }
  ]
})

export default router
