months = ('January','February','March')

print(type(months))
print(months)

numbers = tuple((1,2,3))
print(numbers)

print('**********Tuples - attributes and methods**********')
print(dir(months))

print(months[1])

#Not a tuple
thistuple = ('apple')
print(type(thistuple))
print(thistuple)

#Tuple with one item
tupleOne = ('apple',)
print(type(tupleOne))
print(tupleOne)
