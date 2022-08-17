#One approach
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2) ** 0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

x = li.distance()
print(x)
y = li.slope()
print(y)

#Different approach
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2-y1)/(x2-x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

x = li.distance()
print(x)
y = li.slope()
print(y)

# Cylinder
class Cylinder:

    pi = 3.14

    def __init__(self ,height=1 ,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return (2 * Cylinder.pi * self.radius ** 2 + 2 * self.radius * self.pi * self.height)

# EXAMPLE OUTPUT
c = Cylinder(2,3)

x = c.volume()
print(x)
y = c.surface_area()
print(y)