class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    def calculate_tax(self):
        # Base tax calculation, to be overridden by subclasses
        return 0
    
    def __add__(self, other):
        if isinstance(other, Product):
            total_price = self.get_price() + other.get_price()
            # Calculate weighted average tax rate
            weighted_tax = (self.calculate_tax() * self.get_price() + 
                           other.calculate_tax() * other.get_price()) / total_price
            combo = Product("Combo", total_price)
            # Store the weighted tax as an attribute for the combo product
            combo.weighted_tax = weighted_tax
            return combo
        return NotImplemented
    
    def __str__(self):
        if hasattr(self, 'weighted_tax'):
            # For combo products, show the weighted average tax
            tax_percentage = self.weighted_tax
        else:
            tax_percentage = self.calculate_tax()
        
        return f"Product: {self.name}, Price: {self.get_price()}, Tax: {tax_percentage:.1f}%"


class Electronics(Product):
    def calculate_tax(self):
        return 18.0


class Clothing(Product):
    def calculate_tax(self):
        return 5.0


class Food(Product):
    def calculate_tax(self):
        return 2.0

laptop = Electronics("Laptop", 50000)
tshirt = Clothing("T-Shirt", 1000)

print(laptop)  # Output: Product: Laptop, Price: 50000, Tax: 18.0%
print(tshirt)  # Output: Product: T-Shirt, Price: 1000, Tax: 5.0%

combo = laptop + tshirt
print(combo) 