# Namedtuple

t = (1,2,3)

print(t[0])

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab', name='Micky')

print(sam.age)

print(sam.index('Lab'))

print(sam[0])

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy', claws=False, name='Kitty')

print(c.name)
print(c[2])
print(c[1])