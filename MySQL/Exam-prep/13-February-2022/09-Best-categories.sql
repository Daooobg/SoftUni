SELECT 
    COUNT(*) AS items_count,
    c.`name` AS 'name',
    SUM(p.quantity_in_stock) AS total_quantity
FROM
    categories AS c
        JOIN
    products AS p ON c.id = p.category_id
GROUP BY c.id
ORDER BY items_count DESC , total_quantity
LIMIT 5;