SELECT 
    u.`name` AS university_name,
    c.`name` AS city_name,
    address,
    (IF(tuition_fee < 800,
        'cheap',
        IF(tuition_fee < 1200, 'normal', IF(tuition_fee >= 2500,
            'expensive',
            'high') ))) AS price_rank,
    tuition_fee
FROM
    universities AS u
        JOIN
    cities AS c ON u.city_id = c.id
ORDER BY tuition_fee;
