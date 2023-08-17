-- List all shows
SELECT s.title, sg.genre_id
FROM tv_shows as s JOIN tv_show_genres as sg
	ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
