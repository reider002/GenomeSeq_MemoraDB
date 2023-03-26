<template>
  <div class="shadow p-4 rounded-xl bg-white">
    Dashboard Content
  </div>

</template>


<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      test: 0
    }
  }
}
import { ref } from "vue";
let input = ref("");
const searchID = ["placeholder"];
function filteredList() {
  return searchID.filter((searchID) =>
    searchID.toLowerCase().includes(input.value.toLowerCase())
  );
}
</script>
