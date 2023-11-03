
# Queuekie

Queuekie is an efficient and automated queuing system designed to manage the processing and sorting of orders in your inventory. It leverages the Shortest Job First (SJF) algorithm to optimize order processing, providing a seamless experience for both customers and inventory managers


## Installation

Install these Python Libraries
using pip installation command

Customtkinter	
```
pip install customtkinter

pip install CTkTable

pip install CTkMessagebox
```
PIL	
```
pip install Pillow
```
Mysql-connector-python
```
pip install mysql-connector-python
```
Datetime
```
pip install datetime
```
Time
```
pip install time
```
OS
```
pip install os
```
### ================= Dummy Database Initialization =================

STEP 1: Open XAMPP Command Prompt or MySQL

STEP 2: Start Apache and MySQL

STEP 3: Press Shell and paste the following: ```mysql -h localhost -u root -p``` (Enter Password if you have but usually none unless modified)

STEP 4: Copy paste the following MySql Commands-
```MySQL
create database if not exists queue_system;

use queue_system;

CREATE TABLE orders ( order_id INT PRIMARY KEY, time_ordered TIMESTAMP, sales DECIMAL(10, 2), status VARCHAR(255), time_est VARCHAR(50));

CREATE TABLE cart ( cart_id INT PRIMARY KEY, order_id INT, item_code INT, price DECIMAL(10, 2), quantity INT, amount DECIMAL(10, 2), FOREIGN KEY (order_id) REFERENCES orders(order_id), FOREIGN KEY (item_code) REFERENCES menu(item_code));

CREATE TABLE menu ( item_code INT PRIMARY KEY, item VARCHAR(255), est_time VARCHAR(20), price DECIMAL(10, 2));

CREATE TABLE users ( employee_id VARCHAR(6) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), password VARCHAR(255), logged_in TINYINT(1));

INSERT INTO menu (item_code, item, est_time, price) VALUES (1, 'Fried Chicken w/ Rice', '17 minutes', 95.00), (2, 'Jolly Spaghetti', '12 minutes', 50.00), (3, 'Palabok Fiesta', '13 minutes', 160.00), (4, 'Chicken Sandwich', '7 minutes', 65.00), (5, 'Burger', '6 minutes', 50.00), (6, 'Burger Steak', '8 minutes', 85.00), (7, 'Fries', '4 minutes', 35.00), (8, 'Creamy Macaroni Soup', '3 minutes', 55.00), (9, 'Rice', '3 minutes', 20.00), (10, 'Gravy', 'Instant', 15.00), (11, 'Peach Mango Pie', '2 minutes', 39.00), (12, 'Chocolate Sundae', '1 minute', 39.00), (13, 'Coke', 'Instant', 35.00), (14, 'Sprite', 'Instant', 35.00), (15, 'Pineapple juice', 'Instant', 35.00), (16, 'Hot Chocolate', 'Instant', 35.00), (17, 'Iced Tea', 'Instant', 35.00);

```

After Installation try to run the **"startup.py"**
## Authors

- [@vincentperezzz](https://github.com/vincentperezzz)

- [@doncarlos24](https://github.com/doncarlos24)
