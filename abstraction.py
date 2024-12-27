# Abstract Class
# In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed by other classes. Abstract classes are created using the abc (Abstract Base Classes) module. Abstract classes may contain abstract methods, which are methods that are declared in the abstract class but don't have an implementation. Subclasses of the abstract class are required to provide implementations for these abstract methods.

# Here's an example of an abstract class in Python using the abc module:

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2

# # Example usage:
# circle = Circle(radius=5)
# square = Square(side_length=4)

# print("Circle Area:", circle.area())          # Output: 78.5
# print("Square Area:", square.area())            # Output: 16
# In this example:

# Shape is an abstract class with area as abstract method.
# Circle and Square are concrete classes that inherit from the Shape abstract class and provide implementations for the abstract method.
# Key points about abstract classes in Python:

# Abstract classes cannot be instantiated directly.
# Abstract methods are declared using the @abstractmethod decorator in the abstract class.
# Subclasses must provide concrete implementations for all abstract methods to be considered valid.
# Abstract classes can contain both abstract and non-abstract methods.

from abc import ABC, abstractmethod

# Abstract base class Shape
class Shape:
    # Abstract method for calculating area
    @abstractmethod
    def calculate_area(self):
        pass

# Derived class Square
class Square(Shape):
    def __init__(self, side_length):
        self.side = side_length

    # Implementation of calculate_area for Square
    def calculate_area(self):
        return self.side * self.side

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementation of calculate_area for Rectangle
    def calculate_area(self):
        return self.length * self.width


square_side = int(input('Please enter Length of side of Square: '))
rectangle_length, rectangle_width = list(map(int,input('Please enter Length and Width rectangle, in following format (x y): ').split()))

# Create a Square with a side length
square = Square(square_side)

# Create a Rectangle with length and width
rectangle = Rectangle(rectangle_length, rectangle_width)

# Calculate and display the areas
print('Area of Square is:', square.calculate_area())
print('Area of Rectangle is:', rectangle.calculate_area())

# Vehicle Class Abstraction.
class Vehicle(ABC):
    def __init__(self, n):
        self.name = n

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)

    def start_engine(self):
        print("Car engine started for " + self.name + ".")


car_name = "Nano"

my_car = Car(car_name)
my_car.start_engine()

