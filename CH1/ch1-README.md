# **Challenge 1: E-Commerce System**
## Goal: Design a system for an online store with multiple types of products, each having different taxes applied.

### Requirements
**Encapsulation:**
Product class with private attributes (__price) and getter/setter.

**Inheritance & Polymorphism:**
Electronics, Clothing, Food inherit from Product, each implementing its own calculate_tax().

**Operator Overloading (+):**
Adding two Product objects should merge their price.

**Magic Methods (__str__)**
Print details like Product: Laptop, Price: 50000, Tax: 18%

## Solution 

This system implements all the required features:

### Encapsulation:

The Product class has a private __price attribute with getter/setter methods


### Inheritance & Polymorphism:

Electronics, Clothing, and Food classes inherit from Product
Each subclass overrides the calculate_tax() method with its specific implementation


### Operator Overloading:

The __add__ method allows adding two products to create a combo
It calculates a weighted average tax rate based on the individual product prices


### Magic Methods:

  - __str__ is implemented to print product details in the required format



