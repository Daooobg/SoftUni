-- USED FUNCTION FROM Future Value  

DELIMITER $$
CREATE PROCEDURE usp_calculate_future_value_for_account(acc_id INT, rate DECIMAL(19,4))
BEGIN
	SELECT 
		a.id AS account_id,
		ah.first_name AS first_name,
		ah.last_name AS last_name,
		a.balance AS current_balance,
		(SELECT ufn_calculate_future_value(a.balance, rate, 5)) AS balance_in_5_years
	FROM
		accounts AS a
			JOIN
		account_holders AS ah ON a.account_holder_id = ah.id
	WHERE
		a.id = acc_id;
END $$
DELIMITER ;
;

CALL usp_calculate_future_value_for_account(2, 0.1)