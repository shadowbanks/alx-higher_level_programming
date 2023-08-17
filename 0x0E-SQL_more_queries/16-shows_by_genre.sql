-- Display all genre and tv shows linked to them
SELECT s.title, g.name
FROM tv_shows s
LEFT OUTER JOIN tv_show_genres sg
	ON s.id = sg.show_id
LEFT OUTER JOIN tv_genres g
	ON g.id = sg.genre_id
ORDER BY s.title, g.name;
