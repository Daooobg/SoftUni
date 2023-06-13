SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    address,
    -- MIN(order_datetime) AS order_date
    order_datetime AS order_date
FROM
    customers AS c
        JOIN
    orders AS o ON o.customer_id = c.id
WHERE
    YEAR(order_datetime) <= 2018
-- GROUP BY c.id
ORDER BY full_name DESC;
