-- Lists all genres with the number of shows linked, excluding genres with no shows
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM tv_genres g, tv_show_genres sg
WHERE g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
