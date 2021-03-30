class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
       	self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            return "expects integer or float"

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.y = y
        else:
            return "expects integer or float"

    def set_width(self, width):
        if isinstance(width, (int, float)):
            self.width = width
        else:
            return "expects integer or float"

    def set_height(self, height):
        if isinstance(height, (int, float)):
            self.height = height
        else:
            return "expects integer or float"

    def __str__(self):
        return f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})"

rectangle = Rectangle(5, 10, 50, 100)

print(str(rectangle))