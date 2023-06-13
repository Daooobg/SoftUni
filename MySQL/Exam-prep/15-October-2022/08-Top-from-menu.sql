SELECT 
    p.id, p.`name`, COUNT(*) AS count
FROM
    products AS p
        JOIN
    orders_products AS op ON op.product_id = p.id
GROUP BY p.`name`
HAVING count >= 5
ORDER BY count DESC , p.`name`;