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