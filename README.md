# Real-world Advanced OOP Challenges

Welcome to the repository of real-world advanced OOP challenges that simulate real software development. This repository contains a series of challenges designed to test and improve your object-oriented programming skills.

## Challenge 1: E-Commerce System

### Description
Goal: Design a system for an online store with multiple types of products, each having different taxes applied.

**Requirements:**
- **Encapsulation:** Product class with private attributes (`__price`) and getter/setter.
- **Inheritance & Polymorphism:** Electronics, Clothing, Food inherit from Product, each implementing its own `calculate_tax()`.
- **Operator Overloading (+):** Adding two Product objects should merge their price.
- **Magic Methods (`__str__`):** Print details like Product: Laptop, Price: 50000, Tax: 18%.

### Solution [https://github.com/abhiya492/OOPS_CHALLENGE/blob/master/CH1/P1.py]
This system implements all the required features:

- **Encapsulation:** The Product class has a private `__price` attribute with getter/setter methods.
- **Inheritance & Polymorphism:** Electronics, Clothing, and Food classes inherit from Product. Each subclass overrides the `calculate_tax()` method with its specific implementation.
- **Operator Overloading:** The `__add__` method allows adding two products to create a combo. It calculates a weighted average tax rate based on the individual product prices.
- **Magic Methods:** `__str__` is implemented to print product details in the required format.

## Challenge 2: Employee Management System

### Description
Goal: Build a system for managing employees with different roles and salaries.

**Requirements:**
- **Encapsulation:** Private `__salary` attribute with validation.
- **Inheritance & Polymorphism:** Manager, Developer, Intern inherit Employee, overriding `calculate_bonus()`.
- **Operator Overloading (`>`):** Compare employees based on salary.
- **Magic Method (`__str__`):** Print employee details.

### Solution [https://github.com/abhiya492/OOPS_CHALLENGE/blob/master/CH2/P2.py]
This implementation meets all your requirements:

1. **Encapsulation:** Private `__salary` attribute with getter/setter methods. Validation in the setter ensures salary is a non-negative number.
2. **Inheritance & Polymorphism:** Manager, Developer, and Intern classes inherit from the Employee base class. Each subclass overrides the `calculate_bonus()` method with role-specific bonus calculations.
3. **Operator Overloading:** The `__gt__` (greater than) method allows comparing employees based on their salaries. Returns True if the first employee's salary is greater than the second's.
4. **Magic Methods:** `__str__` is implemented to print employee details in the required format.

## Challenge 3: ATM Simulation

### Description
Goal: Design an ATM system for handling withdrawals, deposits, and transfers.

**Requirements:**
- **Encapsulation:** BankAccount class with a private `__balance`.
- **Operator Overloading (-):** `account1 - account2` transfers balance.
- **Magic Methods (`__str__`):** Print account details.

### Solution  [https://github.com/abhiya492/OOPS_CHALLENGE/blob/master/CH3/P3.py]
The BankAccount class meets all requirements:

1. **Encapsulation:** Private `__balance` attribute with appropriate methods for accessing and modifying it. `deposit()`, `withdraw()`, and `transfer()` methods provide controlled access to the balance.
2. **Operator Overloading:** The `-` operator is overloaded through `__sub__` to transfer the entire balance from one account to another. When you do `account1 - account2`, it transfers all money from `account1` to `account2`.
3. **Magic Methods:** `__str__` method prints account details in the specified format.

## Challenge 4: Ride Sharing App (Like Uber)

### Description
Goal: Design a ride-sharing system where multiple vehicle types have different fare calculations.

**Requirements:**
- **Encapsulation:** Private `__fare_per_km` in Vehicle.
- **Inheritance & Polymorphism:** Bike, Car, SUV override `calculate_fare()`.
- **Magic Methods (`__str__`):** Print ride details.

### Solution  [https://github.com/abhiya492/OOPS_CHALLENGE/blob/master/CH4/p4.py]
The ride-sharing implementation meets all requirements:

1. **Encapsulation:** Private `__fare_per_km` attribute with getter/setter methods.
2. **Inheritance & Polymorphism:** Bike, Car, and SUV classes inherit from the Vehicle base class. Each subclass can override the `calculate_fare()` method (SUV adds a comfort charge).
3. **Magic Methods:** `__str__` method displays vehicle details.
