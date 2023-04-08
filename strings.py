text = 'Python is a programming language that lets you work quickly and integrate systems more effectively'

print(text)

print('**********String - attributes and methods**********')
print(dir(text))

print('**********String - Methods**********')
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text.capitalize())

print(text.replace('Python','Python:'))
print(text.count('y'))

print(text.startswith('Python'))
print(text.startswith('systems'))

print(text.split())

text2 = 'Python is a high-level|general-purpose programming language|Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule'
print(text2.split('|'))
print(text2.find('h')) #start at zero (0)

print(len(text))
print(text2.index('y'))

print(text2.isnumeric())
print(text2.isalpha())

print(text2[0]) #Index
print(text2[-2])

#Another way to concatenate string
print('**********Another way to concatenate string**********')
print("Text: " + text)
print("Text: {0}".format(text))
print(f"Text: {text}") #Since python 3.6