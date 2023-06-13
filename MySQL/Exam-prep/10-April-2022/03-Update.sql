UPDATE movies_additional_info m 
SET 
    m.runtime = m.runtime - 10
WHERE
    m.id BETWEEN 15 AND 25;