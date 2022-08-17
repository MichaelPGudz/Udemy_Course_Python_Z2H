#Inheritance examples
class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i (self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am Milosz and eat shit")

    def bark(self):
        print("WOOF!")

my_dog = Dog()
my_dog.who_am_i()
my_dog.bark()
my_dog.eat()

#Polimorphism examples

class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

# print('\n'*100)

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

def pet_speak(pet):
    print(pet.speak())


for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

#Abstract Class Example
class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says woof"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())
