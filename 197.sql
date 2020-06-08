/* Rising Temperature */
/* https://www.youtube.com/watch?v=8TagsAcEujA */

/* runtime: faster than 61.93% */
SELECT tb1.Id
FROM Weather as tb1
INNER JOIN Weather as tb2
ON tb1.Temperature > tb2.Temperature AND DATEDIFF(tb1.RecordDate, tb2.RecordDate) = 1
WHERE tb1.RecordDate > tb2.RecordDate