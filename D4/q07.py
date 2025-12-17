# Q7. (Medium–Advanced) — Composition
# Create: Engine class
# Car class that uses Engine (not inherits)
# Explain in code why composition is used.

class Engine:
    def start(self):
        print("Engine is starting...")

    def stop(self):
        print("Engine is stopping...")
    
class Car:
    def __init__(self):
         self.engine=Engine()
    
    def drive(self):
        self.engine.start()
        print("Car is moving!")
        self.engine.stop()

car= Car()
car.drive()
     