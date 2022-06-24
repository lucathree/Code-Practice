const loginForm = document.querySelector("#nameForm");
const loginInput = document.querySelector("#nameForm input");
const loginWrapper = document.querySelector("#loginWrapper");
const mainWrapper = document.querySelector("#mainWrapper");
const logoutButton = document.querySelector("#logout");

const USERNAME_KEY = "username";
const HIDDEN = "hidden";

function handleLogin(event) {
    event.preventDefault();
    localStorage.setItem(USERNAME_KEY, loginInput.value);
    paintMain(loginInput.value);
}

function handleLogout(event) {
    event.preventDefault();
    const input = confirm("Do you really want to logout? All of your tasks will be removed.");

    if (input === true) {
        localStorage.removeItem(USERNAME_KEY);
        localStorage.removeItem("tasks");
        document.querySelector("#entered-list").innerHTML = "";
        loginWrapper.classList.add("login-wrapper");
        loginWrapper.classList.remove(HIDDEN);
        mainWrapper.classList.add(HIDDEN);
        mainWrapper.classList.remove("main-wrapper")
    }
}

function paintMain(username) {
    loginWrapper.classList.remove("login-wrapper");
    loginWrapper.classList.add(HIDDEN);
    mainWrapper.classList.remove(HIDDEN);
    mainWrapper.classList.add("main-wrapper")
    const greeting = document.querySelector("#hi");
    greeting.innerText = `Hello ${username},`;
}

function paintLogin() {
    loginWrapper.classList.add("login-wrapper");
    loginWrapper.classList.remove(HIDDEN);
    mainWrapper.classList.add(HIDDEN);
    mainWrapper.classList.remove("main-wrapper")
}

loginForm.addEventListener("submit", handleLogin);
logoutButton.addEventListener("click", handleLogout);

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
    paintLogin();
} else {
    paintMain(savedUsername);
}