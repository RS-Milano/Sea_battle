class Rectangle:
    def __init__(self, a, b):
        self.a = a
       	self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def set_a(self, a):
        if isinstance(a, (int, float)):
            self.a = a
        else:
            return "expects integer or float"

    def set_b(self, b):
        if isinstance(b, (int, float)):
            self.b = b
        else:
            return "expects integer or float"

    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a

    def get_a(self):
        return self.a

    def set_a(self, a):
        if isinstance(a, (int, float)):
            self.a = a
        else:
            return "expects integer or float"

    def get_area(self):
        return self.a ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if isinstance(radius, (int, float)):
            self.radius = radius
        else:
            return "expects integer or float"

    def get_area(self):
        return 3.1415926 * (self.radius ** 2)