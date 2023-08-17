-- List all shows
SELECT s.title, sg.genre_id
FROM tv_shows AS s INNER JOIN tv_show_genres AS sg
	ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
