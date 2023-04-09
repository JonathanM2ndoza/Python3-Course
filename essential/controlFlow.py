
#**********************The if statement**********************

print('*************Nested - if statement*************')
i = 10
if (i == 10):
    #First if statement
    if (i < 15):
        print("i is smaller than 15")
          
    #Nested - if statement
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

print('*************The if statement*************')

x = 20
if (x == 10):
    print("x is 10")
elif (x == 15):
    print("x is 15")
elif (x == 20):
    print("x is 20")
else:
    print("x is not present")

print('*************The if statement and Operators*************')

if (x > 2) and (x <= 50):
    print('x is greater than two and less than or equal to fifty')
if(x > 2) or (x <= 20):
    print('x is greater than two and less than or equal to twenty')
if(not(x == i)):
    print('This result was denied to enter the condition')


print('*************The if statement and lambda function*************')
lambdaOne = lambda a, b : a * b
print(lambdaOne(5, 6)) 

if (lambda x : (x > 2) and (x <= 50)):
    print('x is greater than two and less than or equal to fifty - lambda')

if (lambda x : (x > 2) or (x <= 20)):
    print('x is greater than two and less than or equal to twenty - lambda')

print(f'Result lambda: {(lambda x, y, z=3: x + y + z)(1, 2)}')


#**********************The For & While statement**********************

print('\n*************The For & While statement*************\n')

pets = ['cat', 'dog', 'hamster', 'rabbit','fish','bird']

#Python For loop
print('*************Python For loop*************')
for pet in pets:
    if (pet == 'cat'): 
        print ('My favorite!!')
    print (pet)
    
    if(pet == 'rabbit'):
        print ('Go out the for....') 
        break 
        

sum = 0
for i in range(1, 10):
    sum = sum + i
    #print (sum)
print("\nSum of first 10 numbers :", sum)


#Python While
print('*************Python While*************')
count = 0
while (count <= 3):
    count = count + 1
    print(f"While: {count}" )


n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('While ended.')