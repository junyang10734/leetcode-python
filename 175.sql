/* Combine Two Tables */
/* SQL */

/* runtime: faster than 27.06% of MySQL */
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId;