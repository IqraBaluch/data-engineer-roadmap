DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (customer_id INT, name TEXT);
INSERT INTO customers VALUES
 (1, 'Ali'),
 (2, 'Sara'),
 (3, 'Omar'),
 (4, 'Hina');

CREATE TABLE orders (order_id INT, customer_id INT, amount INT);
INSERT INTO orders VALUES
 (101, 1, 500),
 (102, 1, 300),
 (103, 2, 700),
 (104, 5, 200);


-- 
-- ============================================================
-- Joins · ON vs WHERE in a LEFT JOIN
-- Question: show EVERY customer, with their orders above 400 if any
-- ============================================================

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (customer_id INT, name TEXT);
INSERT INTO customers VALUES
 (1, 'Ali'), (2, 'Sara'), (3, 'Omar'), (4, 'Hina');

CREATE TABLE orders (order_id INT, customer_id INT, amount INT);
INSERT INTO orders VALUES
 (101, 1, 500), (102, 1, 300), (103, 2, 700), (104, 5, 200);


-- Version A: filter in WHERE  ->  WRONG for "every customer"
-- WHERE runs AFTER the join. Omar and Hina have amount = NULL,
-- NULL > 400 is unknown, so WHERE drops them.
-- The LEFT JOIN silently becomes an INNER JOIN.
-- Result: Ali 500, Sara 700
SELECT c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.amount > 400;


-- Version B: filter in ON  ->  CORRECT
-- The filter is part of the matching. Each customer only matches
-- orders above 400; customers with none are still kept, with NULLs.
-- Result: Ali 500, Sara 700, Omar NULL, Hina NULL
SELECT c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o
  ON c.customer_id = o.customer_id
 AND o.amount > 400;


-- RULE
-- Filter on the RIGHT table of a LEFT JOIN:
--   in ON    -> decides which rows match; every left row is kept
--   in WHERE -> removes rows after the join, NULL rows included
--               (LEFT JOIN behaves like INNER JOIN)
-- Ask: "Should customers with no qualifying order still appear?"
--   yes -> ON        no -> INNER JOIN (filter can go in WHERE)
-- For INNER JOIN, ON vs WHERE gives the same result.
