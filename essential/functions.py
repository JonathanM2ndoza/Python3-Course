def add(x, y):
    return x + y
print(add(4,5))

addLambda = lambda x, y: x + y
print (addLambda(8,2))

# *args allows us to pass a variable number of non-keyword arguments to a Python function
def funArgs(arg1, *args):
    print("First argument :", arg1)
    for arg in args:
        print("Next argument through *args :", arg)

funArgs('Hello', 'Welcome', 'to', 'Python')

# **kwargs allows us to pass a variable number of keyword arguments to a Python function
def totalPets(**kwargs):
    print(kwargs, type(kwargs))


totalPets(cat=5, dog=7, rabbit=8)


# Global and Local Variables in Python

a = 1
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)
 
 
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# Inner Functions
def addMessages(func):
    def innerFunction():
        print("This is my first decorator")
        func()
        print("Bye!")
    return innerFunction

@addMessages
def greet():
    print("Hello, World!")

greet()

