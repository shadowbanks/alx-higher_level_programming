-- Display all genre and tv shows linked to them
SELECT g.name, COUNT(g.name) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres sg
	ON g.id = sg.genre_id
JOIN tv_shows s
	ON s.id = sg.show_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
