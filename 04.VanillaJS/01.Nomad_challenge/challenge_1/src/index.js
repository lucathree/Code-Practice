/*
The text of the title should change when the mouse is on top of it.
The text of the title should change when the mouse is leaves it.
When the window is resized the title should change.
On right click the title should also change.
The colors of the title should come from a color from the colors array.
DO NOT CHANGE .css, or .html files.
ALL function handlers should be INSIDE of "superEventHandler"
*/

const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
const hello = document.querySelector("h2");

const superEventHandler = {
  handleMouseOver: function () {
    hello.innerText = "The mouse is here!";
    hello.style.color = colors[0];
  },
  handleMouseLeave: function () {
    hello.innerText = "The mouse is gone!";
    hello.style.color = colors[1];
  },
  handleResize: function () {
    hello.innerText = "You just resized!";
    hello.style.color = colors[2];
  },
  handleRightClick: function () {
    hello.innerText = "That was a right click!";
    hello.style.color = colors[4];
  }
};

hello.addEventListener("mouseover", superEventHandler.handleMouseOver);
hello.addEventListener("mouseleave", superEventHandler.handleMouseLeave);
window.addEventListener("resize", superEventHandler.handleResize);
window.addEventListener("contextmenu", superEventHandler.handleRightClick);
