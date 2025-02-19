class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        # Use setter for validation
        self.set_salary(salary)
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be a non-negative number")
    
    def calculate_bonus(self):
        # Base bonus calculation to be overridden
        return 0
    
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.get_salary() > other.get_salary()
        return NotImplemented
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.name} - Salary: {self.get_salary()}"


class Manager(Employee):
    def calculate_bonus(self):
        # Managers get 30% bonus
        return self.get_salary() * 0.3


class Developer(Employee):
    def calculate_bonus(self):
        # Developers get 20% bonus
        return self.get_salary() * 0.2


class Intern(Employee):
    def calculate_bonus(self):
        # Interns get 5% bonus
        return self.get_salary() * 0.05


dev = Developer("Alice", 80000)
manager = Manager("Bob", 120000)
print(dev)          
print(manager)      
print(manager > dev)  # Output: True (Because 120000 > 80000)