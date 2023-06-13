SELECT 
    first_name, last_name, birthdate, review
FROM
    clients
WHERE
    card IS NULL AND birthdate BETWEEN '1978-01-01' AND '1993-12-31'
ORDER BY last_name DESC , id
LIMIT 5; 