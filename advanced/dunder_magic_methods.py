class Person:
    def __init__(self, name: str, age: int):
        print('Created object..')
        self.__name = name
        self.__age = age

    def __del__(self):
        print('Destroyed object..')

Ange = Person('Angelica','11')

