SELECT 
    SUM(ISNULL(`manager_id`)) AS 'don\'t have a manager'
FROM
    `employees`;