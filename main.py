from circle import Circle
from rectangle import Rectangle

circle = Circle(5)
print("This is area:", circle.area())
print(circle.perimeter())

rectangle = Rectangle(4, 6)
print(rectangle.area())
print("This is perimeter:", rectangle.perimeter())
