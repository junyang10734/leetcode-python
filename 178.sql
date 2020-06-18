/* 178. Rank Scores */

/* https://leetcode.com/problems/rank-scores/discuss/685628/MYSQL-Solution */
/* runtime: faster than 95.28% */
select Score, DENSE_RANK() over (order by score desc) "Rank" 
from Scores
order by "Rank";