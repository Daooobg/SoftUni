CREATE TABLE `logs` (
	log_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    old_sum DECIMAL(19, 4) NOT NULL,
    new_sum DECIMAL(19, 4) NOT NULL
); 
DELIMITER $$

CREATE TRIGGER tr_balance_update
	AFTER UPDATE 
    ON accounts
    FOR EACH ROW
BEGIN
	IF OLD.balance <> NEW.balance
    THEN 
		INSERT INTO `logs`(account_id, old_sum, new_sum)
			VALUES (OLD.id, OLD.balance, NEW.balance);
	END IF;
END$$

DELIMITER ;
;

CREATE TABLE notification_emails(
	id INT AUTO_INCREMENT PRIMARY KEY, 
    recipient INT NOT NULL, 
    `subject` VARCHAR(100) NOT NULL, 
    body TEXT NOT NULL
);

DELIMITER $$

CREATE TRIGGER tr_notification_emails
	AFTER INSERT
    ON `logs`
    FOR EACH ROW
BEGIN
	INSERT INTO notification_emails(recipient, subject, body)
		VALUES(
			NEW.account_id, 
			CONCAT('Balance change for account: ', NEW.account_id),
			CONCAT_WS(' ', 'On', DATE_FORMAT(NOW(), '%b %d %Y at %r'), 'your balance was changed from', NEW.old_sum, 'to', NEW.new_sum)
		);
END$$

DELIMITER ;
;