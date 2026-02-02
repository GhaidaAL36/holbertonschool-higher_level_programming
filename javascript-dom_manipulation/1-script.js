const header_id = document.getElementById('red_header');
const header = document.querySelector('header');
header_id.onclick = changeColor;

function changeColor () {
  header.style.color = '#FF0000';
}
