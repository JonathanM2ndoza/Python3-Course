from datetime import date
from cat import Cat
from dog import Dog

# Test
cat1 = Cat("Thomas",date(2022, 1, 25),False)
print(cat1.name + " is " + str(cat1.calculate_age()) + " years old" )
cat1.purr()
cat1.name = "Thomas Me"
#cat1.name = "Thomas Mendoza"

cat2 = Cat("Mario", date(2022, 1, 25), False)
print(cat2.name + " is " + str(cat2.calculate_age()) + " years old" )
cat2.is_declawed()

dog1 = Dog("Amber", date(2015,7,20))
print(dog1.name + " is " + str(dog1.calculate_age()) + " years old" )
dog1.bark()

print(dog1.allPets)

