/* Second Highest Salary */
/* https://www.cnblogs.com/grandyang/p/5348961.html */

/* runtime: faster than 55.63% */
SELECT MAX(Salary) as SecondHighestSalary FROM Employee 
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)