const loginForm = document.querySelector("#nameForm");
const loginInput = document.querySelector("#nameForm input")
const loginWrapper = document.querySelector("#loginWrapper")
const mainWrapper = document.querySelector("#mainWrapper")

const USERNAME_KEY = "username"
const HIDDEN = "hidden"

function handleLogin(event) {
    event.preventDefault();
    localStorage.setItem(USERNAME_KEY, loginInput.value);
    paintMain(loginInput.value);
}

function paintMain(username) {
    loginWrapper.classList.remove("login-wrapper");
    loginWrapper.classList.add(HIDDEN);
    mainWrapper.classList.remove(HIDDEN);
    const greeting = document.querySelector("#hi")
    greeting.innerText = `Hello ${username},`
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
    loginWrapper.classList.remove(HIDDEN);
    loginForm.addEventListener("submit", handleLogin);
} else {
    paintMain(savedUsername);
}
  