const header = document.querySelector('header');
const updateHeaderElement = document.getElementById('update_header');

updateHeaderElement.onclick = () => {
  header.textContent = 'New Header!!!';
};
