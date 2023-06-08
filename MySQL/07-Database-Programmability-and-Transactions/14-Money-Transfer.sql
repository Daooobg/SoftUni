DELIMITER $$
DROP PROCEDURE usp_transfer_money;
CREATE PROCEDURE usp_transfer_money(from_account_id INT, to_account_id INT, amount DECIMAL(19, 4))
BEGIN
	IF (SELECT id FROM accounts WHERE id=from_account_id) IS NOT NULL
		AND (SELECT id FROM accounts WHERE id=to_account_id) IS NOT NULL
        AND amount > 0 THEN 
			START TRANSACTION;
            UPDATE accounts AS a
            SET a.balance = a.balance - amount
            WHERE a.id = from_account_id;
            UPDATE accounts AS a
            SET a.balance = a.balance + amount
            WHERE a.id = to_account_id;
            IF (SELECT balance FROM accounts WHERE id = from_account_id) < 0  
				THEN 
					ROLLBACK;
				ELSE 
					COMMIT;
			END IF;
     END IF;       
END$$

DELIMITER ;
;

SELECT * FROM accounts;

CALL usp_transfer_money(1, 2, 1000)