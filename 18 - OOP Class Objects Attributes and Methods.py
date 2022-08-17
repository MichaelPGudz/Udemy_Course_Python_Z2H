class Circle():

    #Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius * radius * self.pi

    #Method
    def get_circumference(self):
        #Note that Class Object Attribute Requires the use of a self.
        # prefix when used in method or name of the class itself (i.e. Circle.pi)
        return self.radius * Circle.pi * 2

my_circle = Circle(10)
my_circle.get_circumference()