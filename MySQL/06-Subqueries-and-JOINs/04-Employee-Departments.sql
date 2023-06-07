SELECT 
    employee_id,
    first_name,
    salary,
    departments.`name` AS department_name
FROM
    employees
        JOIN
    departments ON departments.department_id = employees.department_id
WHERE
    salary > 15000
ORDER BY departments.department_id DESC , first_name
LIMIT 5;