DELIMITER $$
CREATE FUNCTION udf_actor_history_movies_count(full_name VARCHAR(50)) 
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE f_name VARCHAR(30);
    DECLARE l_name VARCHAR(30);
    SET f_name := SUBSTRING(full_name,1,  LOCATE(' ', full_name) - 1);
    SET l_name := SUBSTRING(full_name,LOCATE(' ', full_name) + 1);
	RETURN (SELECT COUNT(2) FROM actors AS a
			JOIN movies_actors AS ma ON ma.actor_id = a.id
			JOIN movies AS m ON ma.movie_id = m.id
			JOIN genres_movies AS gm ON m.id = gm.movie_id
			JOIN genres AS g ON gm.genre_id = g.id
			WHERE g.name = 'history' AND a.first_name = f_name AND a.last_name = l_name 
			); 
    
END$$

DELIMITER ;
;

SELECT udf_actor_history_movies_count('Stephan Lundberg')  AS 'history_movies';
SELECT udf_actor_history_movies_count('Jared Di Batista')  AS 'history_movies';


SELECT COUNT(2) FROM actors AS a
JOIN movies_actors AS ma ON ma.actor_id = a.id
JOIN movies AS m ON ma.movie_id = m.id
JOIN genres_movies AS gm ON m.id = gm.movie_id
JOIN genres AS g ON gm.genre_id = g.id

WHERE g.name = 'history' and a.first_name = 'Stephan'