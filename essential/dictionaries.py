#Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

address ={
    'street': 'Lincoln Road',
    'postCode': '33139',
    'city':'Miami',
    'state':'Florida',
    'country': 'United States'
}
customer = {
    'firstName' : 'Jose',
    'lastName' : 'Mendoza',
    'email' : 'xxxx@gmail.com',
    'address': address
}

print(type(customer))
print(customer)

print('**********Dictionary - attributes and methods**********')
print(dir(customer))

print(customer.keys())
print(customer.items())

print(customer.get('firstName'))

print(customer.get('address'))
print(customer['address']['postCode'])

