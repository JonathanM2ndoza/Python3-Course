pets = {'cat', 'dog', 'hamster','cat', 'dog', 'hamster','rabbit','fish'}
print(type(pets))
print(pets)

print('cat' in pets)
pets.add('pig')
print(pets)

print('**********Sets - attributes and methods**********')
print(dir(pets))

pets2 = {'cat', 'rabbit','fish','lizard'}
print(pets2)

allPets = pets.intersection(pets2) #Return a set that contains the items that exist in both set
print(allPets)

print(sorted(allPets))




