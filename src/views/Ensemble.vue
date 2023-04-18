<template>
    <div>
      <button @click="runBiopython()">Run Biopython</button>
      <div v-if="biopythonResult">
        {{ biopythonResult }}
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        biopythonResult: null
      };
    },
    methods: {
      runBiopython() {
          //TODO: replace api call with correct endpoint from Flask Biopython connection
        axios.get('http://rest.ensembl.org/overlap/region/Homo_sapiens/5:112707498-112846239?feature=exon').then(response => {
          console.log(response.data);
        }).catch(error => {
          console.error(error);
        });
      }
    }
  };
  </script>
  