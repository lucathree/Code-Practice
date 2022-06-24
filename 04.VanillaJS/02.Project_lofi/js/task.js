const openTaskButton = document.querySelector("#taskButton")
const taskScreen = document.querySelector("#list-wrapper")

openTaskButton.addEventListener("click", function() {
  taskScreen.classList.toggle("hidden")
});

const taskForm = document.querySelector("#task-form");
const taskInput = document.querySelector("#task-input");
const taskList = document.querySelector("#entered-list");

const TASKS_KEY = "tasks";

let tasks = [];

function paintTask(newTask) {
  const li = document.createElement("li");
  li.id = newTask.id;
  li.className = "list-object"
  const span = document.createElement("span");
  span.innerText = newTask.text;
  const button = document.createElement("span");
  button.innerText = "X";
  button.classList.add("delButton")
  button.addEventListener("click", deleteTask);
  li.appendChild(span);
  li.appendChild(button);
  taskList.appendChild(li);
}

function saveTasks() {
  localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
}

function deleteTask(event) {
  const li = event.target.parentElement;
  li.remove();
  tasks = tasks.filter((task) => task.id !== parseInt(li.id));
  saveTasks();
}

function handleTaskSubmit(event) {
  event.preventDefault();
  const newTask = taskInput.value;
  taskInput.value = "";
  const newTaskObj = {
    text: newTask,
    id: Date.now(),
  };
  tasks.push(newTaskObj);
  paintTask(newTaskObj);
  saveTasks();
}

taskForm.addEventListener("submit", handleTaskSubmit);

const savedTasks = localStorage.getItem(TASKS_KEY);

if (savedTasks !== null) {
  const parsedTasks = JSON.parse(savedTasks);
  tasks = parsedTasks;
  parsedTasks.forEach(paintTask);
}
