DELETE FROM customers AS c
WHERE (SELECT COUNT(*) FROM orders WHERE customer_id = c.id) = 0;