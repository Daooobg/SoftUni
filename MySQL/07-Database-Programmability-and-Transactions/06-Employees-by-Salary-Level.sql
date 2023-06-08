DELIMITER $$
CREATE PROCEDURE usp_get_employees_by_salary_level(level VARCHAR(7))
BEGIN
	SELECT first_name, last_name FROM employees
    WHERE (salary < 30000 AND level = 'Low')
    OR (salary >= 30000 AND salary <= 50000 AND level = 'Average')
    OR (salary > 50000 AND level = 'High')
	ORDER BY first_name DESC, last_name DESC;
END $$
DELIMITER ;
;

CALL usp_get_employees_by_salary_level('High')