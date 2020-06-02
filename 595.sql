/* 595. Big Countries */

/* runtime: faster than 78.63% */
SELECT 
    name, population, area
FROM 
    world
WHERE
    area > 3000000 OR population > 25000000