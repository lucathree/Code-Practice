const clockTitle = document.querySelector(".js-clock");

function getClock() {
  const now = new Date();
  const thisYear = now.getFullYear();
  const xmasEve = new Date(`${thisYear}/12/24`);
  let diff = xmasEve - now;

  if (diff <= 0) {
    const nextXmasEve = new Date(`${thisYear + 1}/12/24`);
    diff = nextXmasEve - now;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = 24 - now.getHours();
  const minutes = 60 - now.getMinutes();
  const seconds = 60 - now.getSeconds();

  clockTitle.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

getClock();
setInterval(getClock, 1000);
