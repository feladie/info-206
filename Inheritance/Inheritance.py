"""
Python class example with Inheritance.
"""

###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Shape(object):
    color = "red"
    coord = 1

    def __init__(self):
        print("Created shape")

    def draw(self):
        print("Drew shape")

    def rotate(self):
        print("Rotated shape")

    def setColor(self, color):
        self.color = color
        print("Changed color for shape")

class Circle(Shape):
    radius = 1

    def __init__(self, radius):
        self.radius = radius
        print("Created circle")

    def draw(self):
        print("Drew circle")

    def computeArea(self):
        print("Comupted area for circle")


class Line(Shape):
    length = 0

    def __init__(self, length = 10):
        self.length = length
        print("Created Line")

    def draw(self):
        print("Drew a line")

class Triangle(Shape):

    angle = 10

    def __init__(self):
        print("Created Triangle")

    def draw(self):
        print("Drew a Triangle")

    def computeArea(self):
        print("Computed area for Triangle")
