from datetime import date

class Pet:
    
    allPets = []

    # init method or constructor
    def __init__(self, name: str, birthDate: date):

        assert (name and not name.isspace()), f"Name {name} can not be empty."
        assert (birthDate != ''), f"BirthDate {birthDate} can not be empty."
        
        self.__name = name
        self.birthDate = birthDate

        Pet.allPets.append(self)
    
    @property
    # Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    # Control to rename 
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
    
    # __repr__ is a special method used to represent a class’s objects as a string. 
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.birthDate}, {self.calculate_age()})"
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day)) #does not include leap years
        return age
    
    @staticmethod
    def count_pets():
        return len(Pet.allPets)
    
    def eat(self):
        print('All pets eat')