from datetime import date
from pet import Pet

class Cat(Pet):
     
     def __init__(self, name: str, birthDate: date,  isDeclawed: bool):
          # Call to super function to have access to all attributes / methods
        super().__init__(
            name, birthDate
        )

        self.isDeclawed = isDeclawed
     
     def purr(self):
         print(f"{self.name} is purring!")
        
     def is_declawed(self):
         if(self.isDeclawed):
             print(f"{self.name} is Declawed")
         else:
            print(f"{self.name} isn't Declawed")
        
    # Example of the Polymorphism
     def eat(self):
         print(f"{self.name} is eating Cat Food")   