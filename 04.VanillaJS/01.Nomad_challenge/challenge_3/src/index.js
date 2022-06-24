const range = document.querySelector("#range");
const guess = document.querySelector("#guess");
const rouletForm = document.querySelector("#roulet");
const status = document.querySelector("#status");
const result = document.querySelector("#result");

function getResult(event) {
  event.preventDefault();
  if (range.value === "" || guess.value === "") {
    alert("Please enter a number");
    status.classList.add("hidden");
    result.classList.add("hidden");
  } else if (range.value <= 0 || guess.value <= 0) {
    alert("Input number should be bigger than 0");
    status.classList.add("hidden");
    result.classList.add("hidden");
  } else {
    let randomNum = Math.ceil(Math.random() * range.value);
    status.innerText = `You chose: ${guess.value}, the machine chose: ${randomNum}.`;
    if (Number(guess.value) === randomNum) {
      result.innerText = "You Won!";
    } else {
      result.innerText = "You Lost!";
    }
    status.classList.remove("hidden");
    result.classList.remove("hidden");
  }
}

rouletForm.addEventListener("submit", getResult);
