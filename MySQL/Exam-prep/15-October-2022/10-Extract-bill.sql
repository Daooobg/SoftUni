DELIMITER $$
CREATE FUNCTION udf_client_bill(full_name VARCHAR(50)) 
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
	DECLARE f_name VARCHAR(30);
    DECLARE l_name VARCHAR(30);
    SET f_name := SUBSTRING(full_name,1,  LOCATE(' ', full_name) - 1);
    SET l_name := SUBSTRING(full_name,LOCATE(' ', full_name) + 1);
	RETURN (SELECT sum(p.price) FROM clients AS c
			JOIN orders_clients AS oc ON oc.client_id = c.id
			JOIN orders_products AS op ON oc.order_id = op.order_id
			JOIN products AS p ON p.id = op.product_id
			WHERE c.`first_name` = f_name AND c.`last_name` = l_name 
			); 
    
END$$

DELIMITER ;
;

SELECT udf_client_bill('Silvio Blyth') ;

SELECT c.first_name,c.last_name, udf_client_bill('Silvio Blyth') as 'bill' FROM clients AS c
WHERE c.first_name = 'Silvio' AND c.last_name= 'Blyth';