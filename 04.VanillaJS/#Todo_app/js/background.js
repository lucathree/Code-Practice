const TOTAL_IMAGES = 18
  
const button = document.querySelector("#shuffle");

button.addEventListener("click", changeBackground)

function changeBackground() {
    const imageNum = Math.floor(Math.random() * TOTAL_IMAGES).toString();
    document.body.style.backgroundImage = `url('./img/bg/${imageNum}.gif')`;
}