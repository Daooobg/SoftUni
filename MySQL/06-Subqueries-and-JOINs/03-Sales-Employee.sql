SELECT 
    employee_id,
    first_name,
    last_name,
    departments.`name` AS department_name
FROM
    employees
        JOIN
    departments ON departments.department_id = employees.department_id
HAVING department_name = 'Sales'
ORDER BY employee_id DESC;