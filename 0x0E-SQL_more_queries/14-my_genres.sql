-- Display all genre and tv shows linked to them
SELECT g.name
FROM tv_genres g
INNER JOIN tv_show_genres sg
	ON g.id = sg.genre_id
INNER JOIN tv_shows s
	ON s.id = sg.show_id
	WHERE s.title = "Dexter"
GROUP BY g.name
ORDER BY g.name;
