-- List all shows by their rating
SELECT s.title, SUM(sr.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings sr ON sr.show_id = s.id
GROUP BY s.title
ORDER BY rating DESC;
