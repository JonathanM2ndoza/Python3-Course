class Person:
    def __init__(self, name: str, age: int):
        print('Created object..')
        self.__name = name
        self.__age = age

    def __del__(self):
        print('Destroyed object..')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__age})"

    def __call__(self):
        print('Invoked object..')

ange = Person('Angelica','11')
print(ange)

ange()


