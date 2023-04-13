import csv

from datetime import date, datetime

class Pet:
    
    allPets = []

    # init method or constructor
    def __init__(self, name: str, type: str,  birthDate: date):

        assert (name and not name.isspace()), f"Name {name} can not be empty."
        assert (type and not type.isspace()), f"Type {type} can not be empty."
        assert (birthDate != ''), f"BirthDate {birthDate} can not be empty."
        
        self.name = name
        self.type = type
        self.birthDate = birthDate

        Pet.allPets.append(self)
    
    # __repr__ is a special method used to represent a class’s objects as a string. 
    def __repr__(self):
        return f"Pet('{self.name}', {self.type}, {self.birthDate}, {self.calculate_age()})"
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day)) #does not include leap years
        return age
    
    # the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName.MethodName()
    @classmethod
    def load_data_from_csv(arg):
        #print(arg.allPets)
        with open('pets.csv', 'r') as file:
            reader = csv.DictReader(file)
            pets = list(reader)

        for pet in pets:
            Pet(
                name=pet.get('name'),
                type=pet.get('type'),
                birthDate=datetime.strptime(pet.get('birthDate'), '%Y-%m-%d')
            )

    @staticmethod
    def count_pets():
        return len(Pet.allPets)



print('***************Static Method**********************')
Pet.load_data_from_csv()
print(Pet.allPets)

print("The are " + str(Pet.count_pets()) + " Pets")
