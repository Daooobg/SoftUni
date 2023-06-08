DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above(supplied_number DECIMAL(10, 4))
BEGIN
	SELECT first_name, last_name FROM employees AS e
	WHERE e.salary >= supplied_number
	ORDER BY e.first_name, e.last_name, e.employee_id;
END $$
DELIMITER ;
;

CALL usp_get_employees_salary_above(45000);