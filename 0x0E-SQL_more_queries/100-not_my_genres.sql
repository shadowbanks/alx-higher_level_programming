-- Display all genre not linked to movie "Dexter"
SELECT DISTINCT g.name
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
WHERE g.id NOT IN (
	SELECT sg.genre_id
	FROM tv_show_genres sg INNER JOIN tv_shows s ON s.id = sg.show_id
	WHERE s.title = "Dexter"
)
ORDER BY g.name;
