const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://tiktok-trending-data.p.rapidapi.com/t',
  headers: {
    'X-RapidAPI-Key': 'f4e78f2d5emshd0942916265cb2cp1474ccjsne654d24f0d80',
    'X-RapidAPI-Host': 'tiktok-trending-data.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});