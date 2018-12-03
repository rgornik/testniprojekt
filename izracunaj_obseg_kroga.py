from math import pi

class Circle(object):

    def __init__(self, r):
        self.r = r

    def area(self):
        return pi*self.r**2

    def circumference(self):
        return 2*pi*self.r

if __name__ == '__main__':
    c1 = Circle(2)
    c2 = Circle(45.2)
    print c1.area()
    print c1.circumference()

    print c2.area()
    print c2.circumference()