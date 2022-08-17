class Dog():

    #Class Object Attribute
    #Same For Any Instance of a Class
    species = 'mammal'

    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name

        #Expect boolean True/False
        self.spots = spots

    # Operations/Actions --> Methods
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and Kicia fucked me over {number} times")

my_dog = Dog('Kundel','Milosz', True)

my_dog.bark(2)