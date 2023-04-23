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

class Dog(Pet):
    def __init__(self, name: str, birthDate: date):
          # Call to super function to have access to all attributes / methods
        super().__init__(
            name, birthDate
        )

    def bark(self):
          print(f"{self.name} is barking!")
    

# Test
cat1 = Cat("Thomas",date(2022, 1, 25),False)
print(cat1.name + " is " + str(cat1.calculate_age()) + " years old" )
cat1.purr()

cat2 = Cat("Mario", date(2022, 1, 25), False)
print(cat2.name + " is " + str(cat2.calculate_age()) + " years old" )
cat2.is_declawed()

dog1 = Dog("Amber", date(2015,7,20))
print(dog1.name + " is " + str(dog1.calculate_age()) + " years old" )
dog1.bark()

print(Pet.allPets)