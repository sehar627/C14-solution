class Car:
    def start(self, car_name):
        print(f"{car_name} has started.")

    def accelerate(self, speed):
        print(f"The car is now moving at {speed} km/h.")

# Creating car objects
red_car = Car()
blue_car = Car()

# Calling methods with parameters
red_car.start("Red Car")  
blue_car.accelerate(80)  
