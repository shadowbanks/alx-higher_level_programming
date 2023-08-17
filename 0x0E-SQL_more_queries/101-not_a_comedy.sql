-- Lists all shows without the genre ``comedy`` in the DB
SELECT DISTINCT s.title
FROM tv_shows s
LEFT OUTER JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT OUTER JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.id NOT IN(
	SELECT sg.show_id FROM tv_show_genres sg
	LEFT OUTER JOIN tv_genres g ON sg.genre_id = g.id
	WHERE g.name = "comedy"
)
ORDER BY s.title;
