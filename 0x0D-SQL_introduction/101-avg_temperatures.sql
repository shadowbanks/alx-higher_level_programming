-- Calculate the average temp (F) by city ordered by temp(descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
