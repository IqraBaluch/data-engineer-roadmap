

SELECT * from customers;
SELECT * from orders;

-- in case of left join, the colum that is comming from right table will have null
-- expect nulls in amount column
select c.customers_id, c.name, o.amount
from orders o
left join customers c
ON c.customers_id = o.customer_id