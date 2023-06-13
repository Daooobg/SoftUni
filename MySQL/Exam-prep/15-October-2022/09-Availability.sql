SELECT 
    t.id AS table_id,
    t.capacity AS capacity,
    COUNT(*) AS count_clients,
    (IF(capacity > COUNT(oc.client_id),
        'Free seats',
        IF(capacity = COUNT(oc.client_id),
            'Full',
            'Extra seats'))) AS availability
FROM
    orders AS o
        JOIN
    `tables` AS t ON o.table_id = t.id
        JOIN
    orders_clients AS oc ON oc.order_id = o.id
WHERE
    t.floor = 1
GROUP BY t.id
ORDER BY t.id DESC;