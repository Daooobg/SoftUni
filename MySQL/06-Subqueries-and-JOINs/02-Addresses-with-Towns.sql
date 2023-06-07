SELECT 
    first_name,
    last_name,
    towns.`name` AS town,
    addresses.address_text AS address_text
FROM
    employees
        JOIN
    addresses ON addresses.address_id = employees.address_id
        JOIN
    towns ON towns.town_id = addresses.town_id
ORDER BY first_name , last_name
LIMIT 5;