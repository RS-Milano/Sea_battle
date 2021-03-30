class Rectangle:
    def __init__(self, width, height):
        self.width = width
       	self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

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

    def get_area(self):
        return self.width * self.height

rectangle = Rectangle(7.3, 16.7)

print(rectangle.get_area())