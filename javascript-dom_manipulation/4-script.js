const addItemElement = document.getElementById('add_item');
const listElement = document.querySelector('.my_list');

addItemElement.onclick = listItem;

function listItem () {
  const li = document.createElement('li');
  li.textContent = 'Item';

  listElement.appendChild(li);
};
