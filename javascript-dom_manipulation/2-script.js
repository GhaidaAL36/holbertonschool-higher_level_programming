const headerId = document.getElementById('red_header');
const header = document.querySelector('header');

headerId.onclick = applyClass;

function applyClass () {
  header.classList.add('red');
}
