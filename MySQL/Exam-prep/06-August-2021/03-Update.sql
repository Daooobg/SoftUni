UPDATE employees
JOIN teams AS t ON t.leader_id = employees.id
SET salary = salary + 1000
WHERE age < 40 AND salary <= 5000;


select * from employees
right JOIN teams AS t ON t.leader_id = employees.id
WHERE age < 40 AND salary <= 5000;