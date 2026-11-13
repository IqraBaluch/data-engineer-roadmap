DROP TABLE IF EXISTS emp;

CREATE TABLE emp(NAME TEXT, DEPARTMENT TEXT, SALARY INT);

INSERT INTO emp VALUES
('Ali',   'IT',    9000),
 ('Sara',  'IT',    7000),
 ('Omar',  'Sales', 8000),
 ('Hina',  'Sales', 5000),
 ('Zain',  'HR',    6000),
 ('Nadia', 'HR',    NULL),
 ('Bilal', NULL,    4000);

 -- Topic 4 · HAVING: filtering the piles

-- Say you want only the departments that have more than one employee. 
-- Try the obvious way first. Type and run:

select department, count(*) as Employees 
from emp 
GROUP BY department 
HAVING count(*) > 1;