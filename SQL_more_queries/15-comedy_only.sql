-- Lists all shows with the genre Comedy, sorted by show title
SELECT s.title
FROM tv_shows s, tv_show_genres sg, tv_genres g
WHERE s.id = sg.show_id
  AND sg.genre_id = g.id
  AND g.name = 'Comedy'
ORDER BY s.title ASC;
