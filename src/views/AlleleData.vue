<template>
    <div class="shadow p-4 rounded-xl bg-white">
      TCGA Mutations from search:
    <table>
      <thead>
        <tr>
          <th>Consequence Type</th>
          <th>Gene Symbol</th>
          <th>Gene ID</th>
          <th>AA Change</th>
          <th>Annotation</th>
          <th>Mutation Subtype</th>
          <th>SSM ID</th>
          <th>Genomic DNA Change</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in Json" :key="item.ssm_id">
          <td>{{ item.consequence.transcript.consequence_type }}</td>
          <td>{{ item.consequence.transcript.gene.symbol }}</td>
          <td>{{ item.consequence.transcript.gene.gene_id }}</td>
          <td>{{ item.consequence.transcript.aa_change }}</td>
          <td>{{ item.consequence.transcript.annotation }}</td>
          <td>{{ item.mutation_subtype }}</td>
          <td>{{ item.ssm_id }}</td>
          <td>{{ item.genomic_dna_change }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </template>
  //TODO: loop throuh items to display in clickable table

  
  <script>
  //TODO: change from local import to API call in data function
  import jsonData from '../Json/consequences-data(1).json'
  export default {
    name: 'AlleleData',
    data: function() {
      return {
        data:jsonData, //passing array data into Vue
      };
    },
    mounted: function() {
        //checking it works
        console.log(this.Json);
    }
  }
  </script>
  