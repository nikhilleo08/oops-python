# Vehicle class Hierarchy
# You are tasked with modeling a simple vehicle hierarchy in Python. Your goal is to create a base class called Vehicle and a derived class called Car.

# Class Definitions:

# Vehicle class:

# Attributes:
# make (String): Represents the make (manufacturer) of the vehicle.
# model (String): Represents the model of the vehicle.
# Methods:
# start(): Prints a message indicating that the vehicle is starting.
# stop(): Prints a message indicating that the vehicle is stopping.
# Car class (inherits from Vehicle):

# Attributes:
# numberOfDoors (int): Represents the number of doors of the car.
# Methods:
# honk(): Prints a message indicating that the car's horn is being honked.
# Additionally, write a Main class with the main method to demonstrate the functionality of these classes. Create instances of both the Vehicle and Car classes, call their methods, and display appropriate messages.

# Expected Output
# Starting the Generic Vehicle
# Stopping the Generic Vehicle
# Starting the Toyota Camry
# Honking the horn of the Toyota Camry
# Stopping the Toyota Camry
# Task
# Complete the code to show that the inheritance and functionality are working correctly.

# Given code
# # Base class
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = ____
#         __________ = model

#     def start(self):
#         print("Starting the", self.make, self.model)

#     def stop(self):
#         print("Stopping the", self.make, self.model)

# # Derived class inheriting from Vehicle
# class Car(Vehicle):
#     def __init__(self, make, model, numberOfDoors):
#         super().__init__(____, _____)
#         self.numberOfDoors = numberOfDoors

#     def honk(self):
#         print("Honking the horn of the", self.make, self.model)


# # Create an instance of the Vehicle class
# generic_vehicle = Vehicle("Generic", "Vehicle")
# _______________.start()
# generic_vehicle.stop()

# # Create an instance of the Car class
# my_car = Car("Toyota", "Camry", 4)
# ______.start()
# my_car.honk()
# my_car.stop()


# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)


# Create an instance of the Vehicle class
generic_vehicle = Vehicle("Generic", "Vehicle")
generic_vehicle.start()
generic_vehicle.stop()

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()


# Hierarchical Inheritance in Vehicle Classes
# You are tasked with modeling a hierarchy of vehicles in Python using hierarchical inheritance. Class Definitions:

# Vehicle class:

# Attributes:
# make (String): Represents the make (manufacturer) of the vehicle.
# model (String): Represents the model of the vehicle.
# Methods:
# start(): Prints a message indicating that the vehicle is starting.
# stop(): Prints a message indicating that the vehicle is stopping.
# Car class (inherits from Vehicle):

# Attributes:
# numberOfDoors (int): Represents the number of doors of the car.
# Methods:
# honk(): Prints a message indicating that the car's horn is being honked.
# Motorcycle class (inherits from Vehicle):

# Attributes:
# engineType (String): Represents the type of engine used in the motorcycle (e.g., "2-stroke" or "4-stroke").
# Methods:
# wheelie(): Prints a message indicating that the motorcycle is performing a wheelie.
# You need to create these classes and implement the methods as described. Additionally, write a Main class with the main method to demonstrate the functionality of these classes.

# Expected Output
# Starting the Toyota Camry
# Honking the horn of the Toyota Camry
# Stopping the Toyota Camry
# Starting the Harley-Davidson Sportster
# Performing a wheelie on the Harley-Davidson Sportster
# Stopping the Harley-Davidson Sportster
# Task
# Complete the code to show that the hierarchical inheritance and functionality are working correctly.

# Given code
# Base class
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = ____
#         __________ = model

#     def start(self):
#         print("Starting the", self.make, self.model)

#     def stop(self):
#         print("Stopping the", self.make, self.model)

# # Derived class Car inheriting from Vehicle
# class Car(Vehicle):
#     def __init__(____, make, model, numberOfDoors):
#         super().__init__(make, model)
#         self._____________ = numberOfDoors

#     def honk(self):
#         print("Honking the horn of the", self.make, self.model)

# # Derived class Motorcycle inheriting from Vehicle
# _____ Motorcycle(Vehicle):
#     def __init__(self, make, model, engineType):
#         super().__init__(make, model)
#         self.engineType = engineType

#     def wheelie(self):
#         print("Performing a wheelie on the", self.make, self.model)

# # Create an instance of the Car class
# my_car = Car("Toyota", "Camry", 4)
# ______.start()
# my_car.honk()
# my_car.stop()

# # Create an instance of the Motorcycle class
# my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", "4-stroke")
# my_motorcycle.start()
# _____________.wheelie()
# my_motorcycle.stop()



# Resolved code
# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)

# Derived class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, engineType):
        super().__init__(make, model)
        self.engineType = engineType

    def wheelie(self):
        print("Performing a wheelie on the", self.make, self.model)

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()

# Create an instance of the Motorcycle class
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", "4-stroke")
my_motorcycle.start()
my_motorcycle.wheelie()
my_motorcycle.stop()


# Constructor Call Sequence
# What is the order of constructor calls when you create an ElectricCar object?

# class Vehicle:
#     def __init__(self):
#         print("Vehicle constructor")

#     def start(self):
#         print("Vehicle started")


# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print("Car constructor")

#     def start(self):
#         print("Car started")


# class ElectricCar(Car):
#     def __init__(self):
#         super().__init__()
#         print("ElectricCar constructor")

#     def start(self):
#         print("ElectricCar started")

# Correct Answer:

# Vehicle constructor -> Car constructor -> ElectricCar constructor
# Explanation:
# In Python, when you create an object of a derived class, the constructor of the base class is called before the constructor of the derived class. This ensures that the base class is fully constructed before any additional construction specific to the derived class takes place. This is known as constructor chaining.


