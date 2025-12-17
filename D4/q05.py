# Q5. (Medium) — Inheritance
# Create: class Vehicle
# class Car (inherits from Vehicle)
# Both should have a method start()
# Override start() in Car.

class Vehicle:
    def start(self):
        print(f"The vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print(f"The Car is starting...")

v=Vehicle()
c=Car()

v.start()
c.start()