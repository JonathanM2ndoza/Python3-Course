from datetime import date

class Pet:
    # init method or constructor
    def __init__(self, name: str, type: str,  birthDate: date):

        assert (name and not name.isspace()), f"Name {name} can not be empty."
        assert (type and not type.isspace()), f"Type {type} can not be empty."
        assert (birthDate != ''), f"BirthDate {birthDate} can not be empty."
        
        self.name = name
        self.type = type
        self.birthDate = birthDate

    def calculate_age(self):
            today = date.today()
            age = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day)) #does not include leap years
            return age
    
    def print_data (self):
         print(self.name)
         print(self.type)
         print(self.birthDate)

pet1 = Pet("Thomas", "Cat", date(2022, 1, 25))
pet2 = Pet("Mario", "Cat", date(2022, 1, 25))
pet3 = Pet("Amber", "Dog", date(2015, 7, 20))

print('*************************************')
pet1.print_data()
print("Is " + str(pet1.calculate_age()) + " years old")
print('*************************************')
pet2.print_data()
print("Is " + str(pet2.calculate_age()) + " years old")
print('*************************************')
pet3.print_data()
print("Is " + str(pet3.calculate_age()) + " years old")

