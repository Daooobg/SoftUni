CREATE TABLE cities (
    city_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50)
);

CREATE TABLE customers (
    customer_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    birthday DATE,
    city_id INT(11),
    CONSTRAINT fk_customers_city_id_cities_city_id FOREIGN KEY (city_id)
        REFERENCES cities (city_id)
);

CREATE TABLE orders (
    order_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    customer_id INT(11),
    CONSTRAINT fk_orders_customer_id_customers_customer_id FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
);

CREATE TABLE item_types (
    item_type_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50)
);

CREATE TABLE items (
    item_id INT(11) AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    item_type_id INT(11),
    CONSTRAINT fk_items_item_type_id_item_types_item_type_id FOREIGN KEY (item_type_id)
        REFERENCES item_types (item_type_id)
);

CREATE TABLE order_items (
    order_id INT(11),
    item_id INT(11),
    CONSTRAINT pk_order_items PRIMARY KEY (order_id , item_id),
    CONSTRAINT fk_order_items_order_id_orders_order_id FOREIGN KEY (order_id)
        REFERENCES orders (order_id),
    CONSTRAINT fk_order_items_item_id_items_item_id FOREIGN KEY (item_id)
        REFERENCES items (item_id)
);