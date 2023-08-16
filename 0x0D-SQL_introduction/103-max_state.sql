-- Calculate the average temp (F) by city ordered by temp(descending)
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY 1;
