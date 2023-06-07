SELECT 
    e.employee_id AS employee_id,
    e.first_name AS first_name,
    IF(DATE(p.start_date) >= '2005-01-01',
        NULL,
        p.`name`) AS project_name
FROM
    employees AS e
        JOIN
    employees_projects AS ep ON ep.employee_id = e.employee_id
        JOIN
    projects AS p ON p.project_id = ep.project_id
WHERE
    e.employee_id = 24
ORDER BY p.`name`;