DELIMITER $$
CREATE PROCEDURE usp_deposit_money (acc_id INT, money_amount DECIMAL(19, 4))
BEGIN
	IF money_amount > 0 THEN
        UPDATE accounts AS a
        SET a.balance = a.balance + money_amount
        WHERE a.id = acc_id;
	END IF;
END $$
DELIMITER ;
;

CALL usp_deposit_money (1, 10);
SELECT 
    *
FROM
    accounts
WHERE
    id = 1;