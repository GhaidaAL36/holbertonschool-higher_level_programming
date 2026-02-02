const moviesElement = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    for (const movie of data.results) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      moviesElement.appendChild(li);
    }
  });
