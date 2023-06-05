SELECT 
    first_name
FROM
    employees
WHERE
    department_id REGEXP '^3|^10'
        AND EXTRACT(YEAR FROM hire_date) BETWEEN 1995 AND 2005
ORDER BY employee_id;