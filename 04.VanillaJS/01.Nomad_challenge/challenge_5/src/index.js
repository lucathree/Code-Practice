const colors = [
  "#ef5777",
  "#575fcf",
  "#4bcffa",
  "#34e7e4",
  "#0be881",
  "#f53b57",
  "#3c40c6",
  "#0fbcf9",
  "#00d8d6",
  "#05c46b",
  "#ffc048",
  "#ffdd59",
  "#ff5e57",
  "#d2dae2",
  "#485460",
  "#ffa801",
  "#ffd32a",
  "#ff3f34"
];

const buttonGet = document.querySelector("#getColor");
const buttonPlay = document.querySelector("#playColor");
const buttonRemove = document.querySelector("#removeColor");
const colorLength = colors.length;
let startPlay = false;
let play;

function getColor() {
  const color1 = colors[Math.floor(Math.random() * colorLength)];
  const color2 = colors[Math.floor(Math.random() * colorLength)];
  const rotation1 = Math.random();
  document.body.style = `background: linear-gradient(${rotation1}turn, ${color1}, ${color2})`;
}


function playColor() {
  startPlay = true;
  play = setInterval(getPlayColor, 150);
  buttonRemove.classList.remove("hidden")
}

function getPlayColor() {
  if (startPlay === true) {
    const color3 = colors[Math.floor(Math.random() * colorLength)];
    const color4 = colors[Math.floor(Math.random() * colorLength)];
    const rotation2 = Math.random();
    document.body.style = `background: linear-gradient(${rotation2}turn, ${color3}, ${color4});
                           transition-duration: 1s;
                           transition-property: background;`;
  }
}

function removeColor() {
  buttonRemove.classList.add("hidden")
  clearInterval(play);
  startPlay = false;
}

buttonGet.addEventListener("click", getColor);
buttonPlay.addEventListener("click", playColor);
buttonRemove.addEventListener("click", removeColor);