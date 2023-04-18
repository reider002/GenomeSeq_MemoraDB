import axios from 'axios';

const baseURL = 'http://localhost:5173'; // Or whatever port you started the server on

axios.get(`${baseURL}/lookup/id/ENSG00000157764?expand=1`)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
