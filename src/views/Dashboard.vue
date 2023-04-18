<template>
  <div class="shadow p-4 rounded-xl bg-white">
    <input type="text" v-model="searchText" placeholder="DNA Change or UUID">
    <button @click="search" class="bg-slate-400 px-4 py-1 rounded-xl mb-4 hover:shadow-lg">Search</button>
    <ul>
      <li v-for="result in results" :key="result.id">{{ result.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchText: '',
      results: [],
    };
  },
  methods: {
    search() {
      //TODO: change placeholder URL, replace with parsed URL containing users search criteria
      axios.get('https://api.gdc.cancer.gov/files/38f3a6d7-7852-5775-858a-2fcaabac54d6?pretty=true', {
        params: {
          q: this.searchText,
        },
      })
        .then(response => {
          this.results = response.data.results;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
</script>
