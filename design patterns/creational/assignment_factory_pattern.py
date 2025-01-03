# Vehicle Factory

# Create a program that uses the Factory Pattern to generate objects of different types of vehicles based on user input. Each vehicle will have unique characteristics and behavior, such as the number of wheels, mode of operation, and purpose.

# Requirements:
# The user can input the type of vehicle they want (e.g., "car," "bike," "truck").
# The program should create the corresponding vehicle object and return its details.
# Each vehicle should implement a method to display its attributes (e.g., number of wheels, type, and primary use).
# Explanation:
# The Factory pattern will abstract the object creation process, allowing the client code to specify the desired vehicle type without worrying about the instantiation details.

from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    def __init__(self, no_of_wheels, type, primary_use):
        self._no_of_wheels = no_of_wheels
        self._vehicle_type = type
        self._primary_use = primary_use

    @abstractclassmethod
    def display(self):
        pass

class Car(Vehicle):
    def display(self):
        print(f'Printing Car: {self._no_of_wheels}, {self._vehicle_type}, {self._primary_use}')

class Truck(Vehicle):
    def display(self):
        print(f'Printing Truck: {self._no_of_wheels}, {self._vehicle_type}, {self._primary_use}')

class Bike(Vehicle):
    def display(self):
        print(f'Printing Bike: {self._no_of_wheels}, {self._vehicle_type}, {self._primary_use}')

class VehicleFactory:
    @staticmethod
    def get_vehicle(type_of_vehicle, no_of_wheels, type, primary_use) -> Vehicle:
        if type_of_vehicle == 'car':
            return Car(no_of_wheels, type, primary_use)
        if type_of_vehicle == 'bike':
            return Bike(no_of_wheels, type, primary_use)
        if type_of_vehicle == 'truck':
            return Truck(no_of_wheels, type, primary_use)
    
vehicle_factory = VehicleFactory()
car = vehicle_factory.get_vehicle('car', 4, 'luxury', 'travelling long distances')
bike = vehicle_factory.get_vehicle('bike', 2, 'standard', 'travelling short')
truck = vehicle_factory.get_vehicle('truck', 10, 'standard', 'delivering goods')
car.display()
bike.display()
truck.display()