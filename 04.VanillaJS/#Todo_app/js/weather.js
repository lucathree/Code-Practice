const city = document.querySelector("#weather span:first-child");
const temperature = document.querySelector("#weather span:nth-child(2)")
const weather = document.querySelector("#weather span:last-child");

const API_KEY = "3cea295e5b64b4a5a7e734b1099dad59";

navigator.geolocation.getCurrentPosition(onSuccess, onFail);

function onSuccess(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  fetchWeather(lat, lon);
}
function onFail() {
  alert("Cound not find your location. Showing default weather.");

  const SEOUL_LAT = 37.568;
  const SEOUL_LON = 126.978;
  fetchWeather(SEOUL_LAT, SEOUL_LON);
}

function fetchWeather(lat, lon) {
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  fetch(url).then((response) => response.json()).then((data) => {
      city.innerText = `${data.name}:`;
      temperature.innerText = `${data.main.temp.toFixed(1)}ºC`;
      weather.innerText = data.weather[0].main;
    });
}
