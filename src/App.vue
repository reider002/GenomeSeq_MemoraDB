<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navigation from './components/Navigation.vue';
</script>

<template>
  <Navigation></Navigation>
  <div class="m-4">
    <RouterView/>
  </div>
</template>

<style scoped>

</style>
