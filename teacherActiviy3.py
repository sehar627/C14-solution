class Car:
    def __init__(self, brand, model, color):  # Constructor to initialize attributes
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.brand} {self.model} has started.")

    def accelerate(self):
        print(f"{self.brand} {self.model} is speeding up!")

# Creating car instances with attributes
red_car = Car("Toyota", "Camry", "Red")
blue_car = Car("Ford", "Mustang", "Blue")

# Calling methods
red_car.start()   # Output: Toyota Camry has started.
blue_car.accelerate()  # Output: Ford Mustang is speeding up!
