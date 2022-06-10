const body = document.querySelector("body");

function colorChange() {
  let size = window.innerWidth;
  if (size < 800) {
    body.className = "windowUnder800";
  } else if (size < 1400) {
    body.className = "windowUnder1400";
  } else {
    body.className = "";
  }
};

window.addEventListener("resize", colorChange);