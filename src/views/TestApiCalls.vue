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
  methods: {
       testCall() {
            //call api
            fetch('https://api.gdc.cancer.gov/files/38f3a6d7-7852-5775-858a-2fcaabac54d6?pretty=true').then((response) => {
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
