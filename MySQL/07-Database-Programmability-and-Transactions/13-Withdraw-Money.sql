DELIMITER $$
CREATE PROCEDURE usp_withdraw_money (acc_id INT, money_amount DECIMAL(19, 4))
BEGIN
	IF money_amount > 0 THEN
		START TRANSACTION;
        UPDATE accounts AS a
        SET a.balance = a.balance - money_amount
        WHERE a.id = acc_id;
        IF (SELECT balance FROM accounts WHERE id = acc_id) < 0 
			THEN
				ROLLBACK;
            ELSE 
				COMMIT;
		END IF;
	END IF;
END $$
DELIMITER ;
;

CALL usp_withdraw_money (1, 10);
SELECT 
    *
FROM
    accounts
WHERE
    id = 1;