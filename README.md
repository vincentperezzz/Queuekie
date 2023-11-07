
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
CREATE TABLE orders ( order_id INT PRIMARY KEY, time_ordered DATETIME, sales DECIMAL(10, 2), status VARCHAR(255), time_est varchar(50), time_finished DATETIME);
```
```
CREATE TABLE menu ( item_code INT PRIMARY KEY, item VARCHAR(255), est_time int, price DECIMAL(10, 2));
```
```
CREATE TABLE cart ( order_id INT, item_code INT, price DECIMAL(10, 2), quantity INT, amount DECIMAL(10, 2), FOREIGN KEY (order_id) REFERENCES orders(order_id), FOREIGN KEY (item_code) REFERENCES menu(item_code));
```
```
CREATE TABLE users ( employee_id VARCHAR(6) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), password VARCHAR(255), logged_in TINYINT(1));
```
```
INSERT INTO menu (item_code, item, est_time, price) VALUES (1, 'Fried Chicken w/ Rice', 17, 95), (2, 'Jolly Spaghetti', 12, 50), (3, 'Palabok Fiesta', 13, 160), (4, 'Chicken Sandwich', 7, 65), (5, 'Burger', 6, 50), (6, 'Burger Steak', 8, 85), (7, 'Fries', 4, 35), (8, 'Creamy Macaroni Soup', 3, 55), (9, 'Rice', 3, 20), (10, 'Gravy', 1, 15), (11, 'Peach Mango Pie', 2, 39), (12, 'Chocolate Sundae', 1, 39), (13, 'Coke', 1, 35), (14, 'Sprite', 1, 35), (15, 'Pineapple juice', 1, 35), (16, 'Hot Chocolate', 1, 35), (17, 'Iced Tea', 1, 35);
```


After Installation try to run the **"startup.py"**


## Algorithm Documentation

### Implementation of the Shortest Job First (SJF) Algorithm in Queue Management
**Introduction:**

The Shortest Job First (SJF) algorithm is a fundamental scheduling and prioritization technique used in queue management systems to optimize order processing. It aims to reduce waiting times for customers by processing orders with the shortest estimated preparation times first. This documentation outlines the approach to implementing the SJF algorithm in a queue management system, particularly when orders have different time of arrival, and a non-preemptive approach is used.

**1. Algorithm Overview:**
The SJF algorithm focuses on the efficient processing of orders by prioritizing those with the shortest estimated preparation times (est-time). In a non-preemptive approach, once an order begins processing, it is allowed to complete without interruption. The algorithm also considers the time of order arrival to ensure fairness when est-time values are equal.

**2. Order Data Structure:**
Orders are represented as tuples containing the following attributes:
```
order_id: A unique identifier for each order.

est-time: The estimated preparation time for the order.

arrival_time: The time at which the order was placed.
```

**3. Sorting Orders:**
The algorithm proceeds as follows:
Initial sorting: Orders are sorted initially by est-time in ascending order.
Handling ties: In cases where est-time values are equal, orders are further sorted by arrival_time in ascending order.

**4. Estimated Finish Time Calculation:**
The estimated finish time for each order is calculated based on the est-time and the order's position in the sorted queue. The formula for calculating the estimated finish time is as follows:
```
Estimated Finish Time = Arrival Time + Estimation Time
```
Arrival Time is converted to minutes.
Estimation Time is the est-time of the order.

**5. Non-Preemptive Processing:**
Once an order begins processing, it is allowed to complete without interruption. This ensures that orders are processed fairly based on their estimated preparation times while minimizing wait times.

**6. Result:**
The result is a prioritized order queue where orders with shorter est-time values are processed first. In cases of equal est-time, orders that arrived earlier are given priority. This approach combines efficiency with fairness to enhance the customer experience.

Comparison with the First Come First Serve let's compare the "First Come, First Serve" (FCFS) and the "Shortest Job First" (SJF) algorithms with examples to illustrate the differences.

***Sample Data***
| Order | Preparation Time (est-time) | Arrival Time | 
|-------|-----------------------------|--------------|
| 1     | 10 minutes                  | 1:00 PM      | 
| 2     | 12 minutes                  | 1:05 PM      | 
| 3     | 8 minutes                   | 1:10 PM      | 
| 4     | 15 minutes                  | 1:15 PM      | 

**First Come First Serve**
| Order | Preparation Time (est-time) | Arrival Time | Finish Time |
|-------|-----------------------------|--------------|------------|
| 1     | 10 minutes                  | 1:00 PM      | 1:10 PM    |
| 2     | 12 minutes                  | 1:05 PM      | 1:22 PM    |
| 3     | 8 minutes                   | 1:10 PM      | 1:30 PM    |
| 4     | 15 minutes                  | 1:15 PM      | 1:45 PM    |

**Shortest Job First**
| Order | Preparation Time (est-time) | Arrival Time | Finish Time |
|-------|-----------------------------|--------------|------------|
| 1     | 10 minutes                  | 1:00 PM      | 1:10 PM    |
| 3     | 8 minutes                   | 1:10 PM      | 1:18 PM    |
| 2     | 12 minutes                  | 1:05 PM      | 1:23 PM    |
| 4     | 15 minutes                  | 1:15 PM      | 1:38 PM    |

**Conclusion:**
FCFS processes orders based on their arrival time, which can lead to longer wait times for orders with longer est-time.

SJF prioritizes efficiency by processing orders with the shortest est-time first, reducing overall wait times.
In this example, SJF leads to faster processing times and potentially happier customers as orders with shorter preparation times are completed earlier.
The choice between FCFS and SJF depends on your specific goals and customer service standards. SJF is a valuable approach for optimizing efficiency, especially in environments where minimizing wait times is a priority.

The implementation of the SJF algorithm in a queue management system, taking into account the differences in order arrival times and using a non-preemptive approach, optimizes order processing. By prioritizing orders with shorter estimated preparation times and considering the time of arrival, the system reduces wait times for customers and ensures a fair processing order. This approach helps to streamline operations and enhance overall customer satisfaction.


## Authors

- [@vincentperezzz](https://github.com/vincentperezzz)

- [@doncarlos24](https://github.com/doncarlos24)
