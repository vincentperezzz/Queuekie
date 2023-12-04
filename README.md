
# Queuekie

Queuekie is an efficient and automated queuing system designed to manage the processing and sorting of orders in your inventory. It leverages the Shortest Job First (SJF) algorithm to optimize order processing, providing a seamless experience for both customers and inventory managers



## Installation

Install these Python Libraries
using pip installation command

Customtkinter	
```
pip install customtkinter
```
```
pip install CTkTable
```
```
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
Threading
```
pip install Threading
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
### ================= Dummy Database Initialization ====================

STEP 1: Open XAMPP Command Prompt or MySQL

STEP 2: Start Apache and MySQL

STEP 3: Press Shell and paste the following: ```mysql -h localhost -u root -p``` (Enter Password if you have but usually none unless modified)

STEP 4: Copy paste the following MySql Commands-
```MySQL
create database queue_system;
```
```
use queue_system;
```
```
CREATE TABLE users ( employee_id VARCHAR(6) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), password VARCHAR(255), logged_in TINYINT(1));
```
```
CREATE TABLE orders ( order_id INT PRIMARY KEY, time_ordered DATETIME, sales DECIMAL(10, 2), status VARCHAR(255), time_est varchar(50), time_finished DATETIME, employee_id VARCHAR(6), FOREIGN KEY (employee_id) REFERENCES users(employee_id));
```
```
CREATE TABLE menu ( item_code INT PRIMARY KEY, item VARCHAR(255), est_time int, price DECIMAL(10, 2));
```
```
CREATE TABLE cart ( order_id INT, item_code INT, price DECIMAL(10, 2), quantity INT, amount DECIMAL(10, 2), FOREIGN KEY (order_id) REFERENCES orders(order_id), FOREIGN KEY (item_code) REFERENCES menu(item_code));
```
```
INSERT INTO menu (item_code, item, est_time, price) VALUES (1, 'Fried Chicken w/ Rice', 17, 95), (2, 'Jolly Spaghetti', 12, 50), (3, 'Palabok Fiesta', 13, 160), (4, 'Chicken Sandwich', 7, 65), (5, 'Burger', 6, 50), (6, 'Burger Steak', 8, 85), (7, 'Fries', 4, 35), (8, 'Creamy Macaroni Soup', 3, 55), (9, 'Rice', 3, 20), (10, 'Gravy', 1, 15), (11, 'Peach Mango Pie', 2, 39), (12, 'Chocolate Sundae', 1, 39), (13, 'Coke', 1, 35), (14, 'Sprite', 1, 35), (15, 'Pineapple juice', 1, 35), (16, 'Hot Chocolate', 1, 35), (17, 'Iced Tea', 1, 35);
```


After Installation try to run the **"startup.py"**


## QUEUEKIE: Queuing System Documentation

### INTRODUCTION 
Queuekie is an automated queuing system that uses the Shortest Job First (SJF) algorithm to prioritize orders based on their processing times. This approach ensures a seamless experience for both customers and inventory managers by minimizing waiting times and contributing to an overall streamlined order fulfillment process.

### Purpose
The purpose of using the Shortest Job First (SJF) algorithm in order processing is to optimize efficiency and customer satisfaction, while also streamlining inventory management. SJF prioritizes orders based on their processing times, which minimizes fulfillment times and provides customers with a faster and more seamless experience.

### Objective 
The objectives of leveraging the Shortest Job First (SJF) algorithm in order processing include optimizing order fulfillment times to enhance customer satisfaction, improving the efficiency of resource utilization, streamlining inventory management, and fostering overall operational agility. By prioritizing orders with the shortest processing times, the algorithm aims to expedite the delivery process, resulting in a more seamless customer experience. 

### The Use of the Algorithm
In a fast-paced restaurant kitchen, where orders arrive in a continuous stream, the Shortest Job First (SJF) algorithm serves as an effective strategy for prioritizing and processing orders efficiently. This algorithm mimics the actions of a skilled chef who meticulously sequences orders based on their preparation times, ensuring that customers receive their meals with minimal wait times.

The SJF algorithm operates by selecting the order with the shortest estimated preparation time among all pending orders. This prioritization ensures that shorter orders are completed promptly, reducing the overall waiting time for customers. Additionally, the algorithm considers the arrival time of each order, preventing newer orders from unfairly overtaking older ones.



## Authors

- [@vincentperezzz](https://github.com/vincentperezzz)

- [@doncarlos24](https://github.com/doncarlos24)
