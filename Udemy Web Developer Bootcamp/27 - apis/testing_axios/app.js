const axios = require('axios');

axios.get('http://api.openweathermap.org/data/2.5/weather?q=chennai&appid=2ffbce013df10d002c54c0a6ecf3f5cf')
  .then(function (response) {
    // handle success
    console.log(response.data);
    let sunrise_time = new Date(response.data.sys.sunrise * 1000);
    console.log("The nex sunset in Chennai is at " + sunrise_time)
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
