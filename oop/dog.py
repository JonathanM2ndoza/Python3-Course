from datetime import date
from pet import Pet

class Dog(Pet):
    def __init__(self, name: str, birthDate: date):
          # Call to super function to have access to all attributes / methods
        super().__init__(
            name, birthDate
        )

    def bark(self):
          print(f"{self.name} is barking!")

    # Example of the Polymorphism
    def eat(self):
        print(f"{self.name} is eating Dog food")   
    
    