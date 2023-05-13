SELECT 
    t.name
FROM
    towns AS t
ORDER BY t.name;
SELECT 
    d.name
FROM
    departments AS d
ORDER BY d.name;
SELECT 
    e.first_name, e.last_name, e.job_title, e.salary
FROM
    employees AS e
ORDER BY e.salary DESC;