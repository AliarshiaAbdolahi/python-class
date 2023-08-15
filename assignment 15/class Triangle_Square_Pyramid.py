class Square:
    def __init__(self, side):
        self.s = side
    def Area(self):
        return (self.s ** 2)
    def Perimeter(self):
        return 4 * self.s

class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)
    def Area(self):
        return (2 * (self.s ** 2)) / 2
    def Perimeter(self):
        return 3 * self.s

class Pyramid(Triangle, Square):
    def __init__(self, height, S_S, S_T):
        self.H = height
        self.S_S = S_S
        self.S_T = S_T
    def Area(self):
        return Square(self.S_S).Area() + (4 * (Triangle(self.S_T).Area()))
    def side_area(self):
        return 4 * (Triangle(self.S_T).Area())
    def volume(self):
        return (self.S_S * self.S_T * self.H) / 3
    
S_S = float(input("Penter emter side of square: "))
T_S = float(input("Please enter side of triangle: "))
P_H = float(input("Please enter height of pyramid: "))

square = Square(S_S)
triangle = Triangle(T_S)
pyramid = Pyramid(P_H, S_S, T_S)

print("square=>\narea:", square.Area(), "\nperimeter:", square.Perimeter())
print("triangle=>\narea:", triangle.Area(), "\nperimeter:", triangle.Perimeter())
print("pyramid=>\narea:", pyramid.Area(), "\nvolume:", pyramid.volume(), "\nside_area:", pyramid.side_area())