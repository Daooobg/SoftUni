UPDATE universities
SET tuition_fee  = tuition_fee + 300
WHERE id BETWEEN 5 and 12;


SELECT * FROM universities
WHERE id BETWEEN 5 and 12