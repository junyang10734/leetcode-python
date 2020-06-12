/* Employees Earning More Than Their Managers */

/* runtime: faster than 50.93% */
SELECT a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
    ON a.ManagerId = b.Id
    AND a.Salary > b.Salary