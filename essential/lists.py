mixList = [1,'Hi',5.2,[5,4,3]]
print(mixList)

pets = ['cat', 'dog', 'hamster']

numbersList = list(range(1,9))
print(numbersList)

print('**********list - attributes and methods**********')

print(dir(pets))

print(len(pets))
print(pets[0])
print('hamster'in pets)

pets.append('turtle')
print(pets)

pets.extend(['rabbit','fish']) #List
print(pets)
pets.extend(('bird','pig')) #Tuple
print(pets)
pets.insert(len(pets),'lizard')
print(pets)

pets.pop()
print(pets)
pets.pop(3)
print(pets)
pets.remove('bird')
print(pets)

pets.sort()
print(pets)
pets.sort(reverse=True)
print(pets)
print(pets.index('cat'))

#Remove Duplicates
pets2 = ['cat', 'dog', 'hamster','cat', 'dog', 'hamster']
print(pets2)
pets2 = list(dict.fromkeys(pets2)) #Create a dictionary and convert a list
print(pets2)

