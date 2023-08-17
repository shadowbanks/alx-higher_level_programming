-- Display all genre and tv shows linked to them
SELECT s.title
FROM tv_genres g
INNER JOIN tv_show_genres sg
	ON g.id = sg.genre_id
INNER JOIN tv_shows s
	ON s.id = sg.show_id
WHERE g.name = "comedy"
GROUP BY s.title
ORDER BY s.title;
