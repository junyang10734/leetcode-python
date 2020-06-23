/* Duplicate Emails */

/* runtime: faster than 72.61% */
SELECT Email
FROM Person
group by Email
having count(Email) > 1;