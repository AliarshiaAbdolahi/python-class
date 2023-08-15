from math import pi

class Circle:
    def __init__(self, R):
        self.R = R
    def Area(self):
        return pi * (self.R ** 2)
    def Perimeter(self):
        return 2 * pi * self.R

class Sphere(Circle):
    def __init__(self, R):
        super().__init__(R)

    def Area(self):
        return 4 * super(). Area()
    def Perimeter(self):
        return super().Area() * self.R  * (4/3)\


radius = float(input("Please enter radius: "))
print()
circle = Circle(radius)
sphere = Sphere(radius)
print("circle\n1_area:", circle.Area(), "\n2_perimeter:", circle.Perimeter())
print("sphere\n1_area:", sphere.Area(), "\n2_perimeter:", sphere.Perimeter())