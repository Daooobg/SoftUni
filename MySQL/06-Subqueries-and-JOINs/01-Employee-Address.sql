SELECT 
    employee_id,
    job_title,
    employees.address_id AS address_id,
    address_text
FROM
    employees
        JOIN
    addresses ON employees.address_id = addresses.address_id
ORDER BY address_id
LIMIT 5;