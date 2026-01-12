-- Lists all genres linked to the show Dexter, sorted by genre name
SELECT g.name
FROM tv_genres g, tv_show_genres sg, tv_shows s
WHERE g.id = sg.genre_id
  AND s.id = sg.show_id
  AND s.title = 'Dexter'
ORDER BY g.name ASC;
