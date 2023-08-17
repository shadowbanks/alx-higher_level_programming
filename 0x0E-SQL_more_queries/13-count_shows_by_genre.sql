-- Display all genre and tv shows linked to them
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres sg
	ON g.id = sg.genre_id
INNER JOIN tv_shows s
	ON s.id = sg.show_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
