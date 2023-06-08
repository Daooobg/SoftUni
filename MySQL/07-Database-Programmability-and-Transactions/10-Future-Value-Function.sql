DELIMITER $$
CREATE FUNCTION  ufn_calculate_future_value(sum DECIMAL(19,4), rate DOUBLE, years INT)
RETURNS DECIMAL(19,4)
DETERMINISTIC
BEGIN
	RETURN  sum * (POWER((1 + rate), years));
END $$

DELIMITER $$

SELECT ufn_calculate_future_value(1000, 0.5, 5)