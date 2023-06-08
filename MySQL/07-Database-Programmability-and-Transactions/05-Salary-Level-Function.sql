DELIMITER $$
CREATE FUNCTION ufn_get_salary_level(received_salary DECIMAL(19,4))
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
	RETURN (
		CASE
			WHEN received_salary < 30000 THEN 'Low'
            WHEN received_salary <= 50000 THEN 'Average'
            ELSE 'High'
        END    
    );
END$$

DELIMITER ;
;

SELECT ufn_get_salary_level(500000000)