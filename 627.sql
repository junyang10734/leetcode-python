/* Swap Salary */

/* runtime: faster than 48.95% */
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' Then 'f'
        ELSE 'm'
    END