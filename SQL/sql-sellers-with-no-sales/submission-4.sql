-- Write your query below
-- find sellers who made sales in the year 2020
SELECT seller_name 
FROm seller 
WHERE seller_id NOT IN
(SELECT o.seller_id
FROM seller s JOIN orders o
ON o.seller_id = s.seller_id
WHERE o.sale_date BETWEEN '2020-01-01' AND '2020-12-31')
ORDER BY seller_name ASC;