SET SQL_SAFE_UPDATES=0;

CREATE TABLE `t_high_paid` AS SELECT * FROM
    `employees`
WHERE
    `salary` > 30000;
    

    
DELETE FROM `t_high_paid` 
WHERE
    `manager_id` = 42;
    
UPDATE `t_high_paid`
SET 
    `salary` = `salary` + 5000
WHERE
    `department_id` = 1;
    
SELECT 
    `department_id`, AVG(`salary`) AS avg_salary
FROM
    `t_high_paid`
GROUP BY `department_id`
ORDER BY `department_id`;