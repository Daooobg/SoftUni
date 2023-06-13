INSERT INTO reviews (content, picture_url, published_at, rating)
	(
		SELECT 
				substring(description, 1, 15),
				REVERSE(`name`),
                '2010-10-10',
                (price / 8)
                FROM products
                WHERE id >=  5
        
    );
    
    
    
    
    