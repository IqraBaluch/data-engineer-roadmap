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


-- Topic 2 · SUM, AVG, MIN, MAX and the NULL surprise

-- These also skip NULLs. The salaries are 9000, 7000, 8000, 5000, 6000, NULL 
-- (Nadia) and 4000, adding up to 39000.

-- Predict the average before running. Is it:

-- A) 39000 ÷ 7 employees = 5571
-- B) 39000 ÷ 6 employees with a salary = 6500

SELECT SUM(SALARY) AS TOTAL,
    AVG(SALARY) AS AVERAGE,
    MIN(SALARY) AS LOWEST,
    MAX(SALARY) AS HIGHEST

FROM emp;