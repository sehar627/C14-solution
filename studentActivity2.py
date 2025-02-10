class NanoBot:
    def move(self, direction, speed):
        print(f"The NanoBot is moved {direction} at speed {speed}.")

    def fire(self, weapon):
        print(f"The NanoBot fired a {weapon}.")

    def reset(self, position):
        print(f"The NanoBot position has been reset to {position}.")

# Creating an object of NanoBot class
nano_bot = NanoBot()

# Calling methods with parameters
nano_bot.move("left", 5)
nano_bot.fire("laser")
nano_bot.reset("starting point")
