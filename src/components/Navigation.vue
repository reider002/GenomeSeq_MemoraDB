<template>
  <header>
    <nav class="shadow p-4 flex items-center bg-gray-700">
        <h1 class="mr-8 text-xl text-white">Cancer Research Appliation</h1>
        <div v-for="link of links" class="mr-4 px-4 py-2 bg-white rounded-xl">
            <RouterLink  :to="link.path" >{{link.name}}</RouterLink>
        </div>
      </nav>
  </header>
</template>

<script>
export default({
    name: 'Navigation',
    data() {
        return {
            reuqestResult: 'Empty',
            links: [
                {
                    name: 'GDC Dashboard',
                    path: '/'
                },
                {
                    name: 'Test API Calls',
                    path: '/test-api-calls'
                },
                {
                    name: 'GDC Allele Data',
                    path: '/allele-data'
                }
            ]
        }
    },
    methods: {
       testCall(){
            //call api
            fetch('www.google.com').then((val) => console.log(val)).catch((err) => console.log(err))
            this.reuqestResult = 'call made';
       } 
    },
    mounted() {
        //call stuff on pageload
    }
})
</script>

<style scoped>

</style>