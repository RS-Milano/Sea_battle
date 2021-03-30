from class_geometric_figures import Rectangle, Square, Circle

rectangle_1 = Rectangle(3, 4)
rectangle_2 = Rectangle(12, 5)

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(3)
circle_2 = Circle(7)

figures = [rectangle_1, rectangle_2, square_1, square_2, circle_1, circle_2]

i = 1
for figure in figures:
    print(f"figure {i} area: ", figure.get_area())
    i += 1