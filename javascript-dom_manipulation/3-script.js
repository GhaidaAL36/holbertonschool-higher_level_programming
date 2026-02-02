const headerId = document.getElementById('toggle_header');
const header = document.querySelector('header');

headerId.onclick = toggles;

function toggles () {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.toggle('red');
  } else {
    header.classList.remove('red');
    header.classList.toggle('green');
  };
};
