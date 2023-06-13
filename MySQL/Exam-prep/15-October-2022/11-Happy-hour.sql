DELIMITER $$
CREATE PROCEDURE udp_happy_hour (product_type VARCHAR(50))
BEGIN
	UPDATE products 
		SET price = price - (price * 0.2)
        WHERE product_type = products.`type` AND products.price >= 10;
END $$

DELIMITER ;
;

CALL udp_happy_hour('Cognac');

SELECT * FROM products
WHERE type = 'Cognac';