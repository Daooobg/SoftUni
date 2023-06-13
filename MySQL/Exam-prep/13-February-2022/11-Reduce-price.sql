DELIMITER $$
DROP PROCEDURE udp_reduce_price;
CREATE PROCEDURE udp_reduce_price (category_name VARCHAR(50))
BEGIN 
UPDATE products AS p
	JOIN categories AS c ON c.id = p.category_id
    JOIN reviews AS r ON p.review_id = r.id
	SET p.price = p.price - (p.price * 0.3 )
    WHERE c.`name` = category_name AND r.rating < 4;
	
END$$

DELIMITER ;
;

CALL udp_reduce_price('Phones and tablets');

SELECT * FROM products AS p
JOIN categories AS c ON c.id = p.category_id
JOIN reviews AS r ON p.review_id = r.id
WHERE p.category_id = 1;
