DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users (user_id INT, join_date DATE, favorite_brand TEXT);
INSERT INTO Users VALUES
 (1, '2018-01-01', 'Lenovo'),
 (2, '2018-02-09', 'Samsung'),
 (3, '2018-01-19', 'LG'),
 (4, '2018-05-21', 'HP');

CREATE TABLE Orders (order_id INT, order_date DATE, item_id INT, buyer_id INT, seller_id INT);
INSERT INTO Orders VALUES
 (1, '2019-08-01', 4, 1, 2),
 (2, '2018-08-02', 2, 1, 3),
 (3, '2019-08-03', 3, 2, 3),
 (4, '2018-08-04', 1, 4, 2),
 (5, '2018-08-04', 1, 3, 4),
 (6, '2019-08-05', 2, 2, 4);

select u.user_id as u.buyer_id, u.join_date, u.orders_in_2019
 from users u
LEFT JOIN orders o
on u.user_id = o.buyer_id
where EXTRACT(YEAR FROM order_date) = 2019
