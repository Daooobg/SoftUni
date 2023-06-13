CREATE DATABASE exam_13_February_2022;
USE exam_13_February_2022;

CREATE TABLE brands (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE categories (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE reviews (
	id INT PRIMARY KEY AUTO_INCREMENT,
    content TEXT,
    rating DECIMAL(10, 2) NOT NULL,
    picture_url VARCHAR(80) NOT NULL, 
    published_at DATETIME NOT NULL
);

CREATE TABLE products (
	id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL,
    price DECIMAL(19,2) NOT NULL,
    quantity_in_stock INT,
    `description` TEXT,
    brand_id INT NOT NULL,
    category_id INT NOT NULL,
    review_id INT NOT NULL,
    CONSTRAINT fk_products_brand_id_brands_id
		FOREIGN KEY (brand_id)
        REFERENCES brands(id),
	CONSTRAINT fk_products_category_id_categories_id
		FOREIGN KEY (category_id)
        REFERENCES categories(id),
	CONSTRAINT fk_products_review_id_reviews_id
		FOREIGN KEY (review_id)
        REFERENCES reviews(id)
);

CREATE TABLE customers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    phone VARCHAR(30) NOT NULL UNIQUE,
    address VARCHAR(60) NOT NULL,
    discount_card BIT(1) NOT NULL DEFAULT FALSE
);

CREATE TABLE orders (
	id INT PRIMARY KEY AUTO_INCREMENT,
    order_datetime DATETIME NOT NULL,
    customer_id INT NOT NULL,
    CONSTRAINT fk_orders_customer_id_customers_id
		FOREIGN KEY (customer_id)
        REFERENCES customers(id)
);

CREATE TABLE orders_products (
	order_id INT,
    product_id INT,
    CONSTRAINT fk_orders_products_order_id_orders_id
		FOREIGN KEY (order_id)
        REFERENCES orders(id),
	CONSTRAINT fk_orders_products_product_id_products_id
		FOREIGN KEY (product_id)
        REFERENCES products(id)
);