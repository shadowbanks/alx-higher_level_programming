-- Display all show including the ones with no genre
SELECT s.title, sg.genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
	ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id
