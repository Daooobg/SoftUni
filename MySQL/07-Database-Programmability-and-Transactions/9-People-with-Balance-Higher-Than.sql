DELIMITER $$
CREATE PROCEDURE usp_get_holders_with_balance_higher_than(amount DECIMAL(19, 4))
BEGIN
	SELECT 
    first_name, last_name
	FROM
		account_holders AS ah
			JOIN
		(SELECT 
			account_holder_id, SUM(accounts.balance) AS total_balance
	FROM
			accounts
	GROUP BY accounts.account_holder_id) AS a ON a.account_holder_id = ah.id
	WHERE
		total_balance > amount
	ORDER BY ah.id;
END $$
DELIMITER ;
;

CALL usp_get_holders_with_balance_higher_than(7000)