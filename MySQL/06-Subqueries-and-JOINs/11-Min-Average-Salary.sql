SELECT 
    AVG(salary) AS avg_salary
FROM
    employees AS e
GROUP BY e.department_id
ORDER BY avg_salary
LIMIT 1;