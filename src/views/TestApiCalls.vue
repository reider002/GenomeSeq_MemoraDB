<template>
  <div class="">
    <h1 class="text-black mb-4">Test Api Calls</h1>
    <button @click="testCall" class="bg-red-600 px-4 py-2 rounded-xl mb-4 hover:shadow-lg">Test Call</button>
    <p v-if="reuqestResult != 'Empty'">{{ reuqestResult }}</p>
    <p v-else>Make an api call first</p>    
  </div>
</template>


<script>
export default({
  name: 'TestApiCalls',
  data() {
    return {
      reuqestResult: 'Empty'
    }
  },
  computed: {
    //TODO: Add search filters here 
  },
  methods: {
       testCall() {
            //call api
            fetch('http://nov2020.archive.ensembl.org/Homo_sapiens/Export/Output/Location?db=core;flank3_display=0;flank5_display=0;g=ENSG00000134982;output=csv;r=5:112707498-112846239;strand=feature;param=similarity;param=repeat;param=genscan;param=variation;param=gene;misc_set=RPCI-11;misc_set=CHORI-17;misc_set=encode;misc_set=tilepath;misc_set=ABC;misc_set=WIBR-2;misc_set=encode_excluded;_format=Text').then((response) => {
              console.log(response);
              response.text().then((result) => this.reuqestResult = result);
            } 
            ).catch((err) => console.log(err));
      } 
  },
  mounted() {
        //call stuff on pageload
  }
})  
</script>

<style>
</style>
