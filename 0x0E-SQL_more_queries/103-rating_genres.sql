-- List all genre based on their rating
SELECT g.name, SUM(sr.rate) AS rating
FROM tv_genres g
INNER JOIN tv_show_genres sg ON sg.genre_id = g.id
INNER JOIN tv_show_ratings sr ON sr.show_id = sg.show_id
GROUP BY g.name
ORDER BY rating DESC;
