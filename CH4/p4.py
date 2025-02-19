class Vehicle:
    def __init__(self, model, fare_per_km):
        self.model = model
        self.__fare_per_km = fare_per_km
    
    def get_fare_per_km(self):
        return self.__fare_per_km
    
    def set_fare_per_km(self, fare):
        if fare > 0:
            self.__fare_per_km = fare
    
    def calculate_fare(self, distance_km):
        base_fare = distance_km * self.__fare_per_km
        return f"Ride Cost: {base_fare} ({distance_km}km × {self.__fare_per_km})"
    
    def __str__(self):
        return f"{self.__class__.__name__} - {self.model} - Fare per km: {self.__fare_per_km}"


class Bike(Vehicle):
    def calculate_fare(self, distance_km):
        # Bikes use standard rate calculation
        return super().calculate_fare(distance_km)


class Car(Vehicle):
    def calculate_fare(self, distance_km):
        # Cars use standard rate calculation
        return super().calculate_fare(distance_km)


class SUV(Vehicle):
    def calculate_fare(self, distance_km):
        # SUVs add a comfort charge of 50
        base_fare = distance_km * self.get_fare_per_km()
        comfort_charge = 50
        total_fare = base_fare + comfort_charge
        return f"Ride Cost: {total_fare} ({distance_km}km × {self.get_fare_per_km()} + {comfort_charge} comfort charge)"


bike = Bike("Honda", 10)
car = Car("Toyota", 50)
suv= SUV("Ford", 100)

print(bike.calculate_fare(5))  # Ride Cost: 50 (5km × 10)
print(car.calculate_fare(5))   # Ride Cost: 100 (5km × 50)
print(suv.calculate_fare(5))   # Ride Cost: 150 (5km × 100 + 50 comfort charge)
