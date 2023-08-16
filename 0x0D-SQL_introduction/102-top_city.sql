-- Calculate the average temp (F) by city ordered by temp(descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY 2 DESC
LIMIT 3;
