# Vehicle MAnagemnet System
class Vehicle:
    def __init__(self, make, model, color, year, price):
        self.make = make
        self. model = model
        self.color = color
        self.year = year
        self.price = price
        
    def display(self):
        return(f"It's a {self.year} {self.make} {self.model} of {self.color} color having price of {self.price}$.")
    
class Car(Vehicle):
    def __init__(self, make, model, color, year, price, doors, fuel_type):
        super().__init__(make, model, color, year, price)
        self.doors = doors
        self.fuel_type = fuel_type
    
    def display(self):
        return(f"It's a {self.year} {self.make} {self.model} of {self.color} color having {self.doors} doors, {self.fuel_type} operated and with a price of {self.price}$.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, color, year, price, engine_size, type):
        super().__init__(make, model, color, year, price)
        self.engine_size = engine_size
        self.type = type
        
    def display(self):
        return(f"It's a {self.year} {self.make} {self.model} {self.type} of {self.color} color having {self.engine_size} engine capacity with a price of {self.price}$.")
    
class Truck(Vehicle):
    def __init__(self, make, model, color, year, price, bed_size, four_wheel_drive):
        super().__init__(make, model, color, year, price)
        self.bed_size = bed_size
        self.four_wheel_drive = four_wheel_drive
        
    def display(self):
        if self.four_wheel_drive == True:
            return(f"It's a {self.year} {self.bed_size} a four wheel drive {self.make} {self.model} of {self.color} color with a price of {self.price}$.")
        else:
            return(f"It's a {self.year} {self.bed_size} {self.make} {self.model} of {self.color} color with a price of {self.price}$.")
        
car1 = Car("Toyota", "Camry", "Red" , 2022, 25000, 4, "Gasoline")
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", "Black", 2020, 12000, "1200cc", "Cruiser")
truck1 = Truck("Ford", "F-150", "Silver", 2019, 35000, "Short", True)

# Display details of each vehicle
print(car1.display())
print(motorcycle1.display())
print(truck1.display())

