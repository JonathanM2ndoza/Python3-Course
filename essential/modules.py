# In Python, a module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__ 

import math, datetime
from myModule import add, substract

x = 2.9
print(math.ceil(x))

currentDate = datetime.datetime.now()
print('Current Date:', currentDate)

# Represent Dates in numerical format
print("dd-mm-yyyy HH:MM:SS:", currentDate.strftime("%d-%m-%y %H:%M:%S"))
print("dd-mm-yyyy:", currentDate.strftime("%d-%m-%Y"))
print("dd-mm-yy Format:", currentDate.strftime("%d-%m-%y"))

# Local module
add(3,9)
substract(10,4)

# The Python Package Index (PyPI) is a repository of software for the Python programming language.
# https://pypi.org/

