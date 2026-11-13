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

-- Seven employees. Notice two gaps: Nadia has no salary yet, and Bilal has no department.

--Topic 1 · Three kinds of COUNT

-- COUNT(*) counts rows.
-- COUNT(column) counts rows where that column is not NULL.
-- COUNT(DISTINCT column) counts different non-NULL values.

-- Before running anything, predict the four numbers this returns:
SELECT COUNT(*)                   AS total_rows,
       COUNT(salary)              AS with_salary,
       COUNT(department)          AS with_department,
       COUNT(DISTINCT department) AS distinct_departments
FROM emp;