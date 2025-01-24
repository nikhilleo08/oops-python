# Problem Statement: Car Rental System
# You're building a Car Rental System where users can rent different types of cars, such as Sedan, SUV, and Convertible. The cars have some basic features like Mileage and Fuel Efficiency. However, you also want to add additional features to these cars such as GPS, Leather Seats, and Sunroof.

# Instead of creating multiple classes for each car type with all possible combinations of features (which would lead to a lot of duplication and complexity), you decide to use the Decorator Pattern to dynamically add features to the cars as needed.

# Requirements:
# Base Class: A Car class with basic features like Mileage and Fuel Efficiency.
# Concrete Classes: Different types of cars, such as Sedan and SUV.
# Decorator Classes: Additional features like GPS, and Sunroof that can be added to any car type dynamically.
# The system should allow users to add any combination of features to the cars without needing to create new classes for every combination.

# class Car():
#     def __init__(self):
#         self._brand = None
#         self._model = None
#         self._mileage = None
#         self._type_of_car = None
    
#     @property
#     def mileage(self):
#         return self._mileage
    
#     @property
#     def model(self):
#         return self._model
    
#     @property
#     def brand(self):
#         return self._brand
    
#     def mileage(self):
#         pass
    
#     def start(self):
#         pass
    
#     def stop(self):
#         pass

# class Sedan(Car):
#     def __init__(self, brand, model, mileage,):
#         self._brand = brand
#         self._model = model
#         self._mileage = mileage
#         self._type_of_car = "Sedan"
#         print('Initialized Sedan')
    
#     @property
#     def mileage(self):
#         return self._mileage
    
#     @property
#     def model(self):
#         return self._model
    
#     @property
#     def brand(self):
#         return self._brand
    
#     def start(self):
#         print(f'Starting Engine for {self._type_of_car} {self.brand} {self.model}')
    
#     def stop(self):
#         print(f'Stopping Engine for {self._type_of_car} {self.brand} {self.model}')


# class SUV(Car):
#     def __init__(self, brand, model, mileage,):
#         self._brand = brand
#         self._model = model
#         self._mileage = mileage
#         self._type_of_car = "SUV"
#         print('Initialized SUV')
    
#     @property
#     def mileage(self):
#         return self._mileage
    
#     @property
#     def model(self):
#         return self._model
    
#     @property
#     def brand(self):
#         return self._brand
    
#     def start(self):
#         print(f'Starting Engine for {self._type_of_car} {self.brand} {self.model}')
    
#     def stop(self):
#         print(f'Stopping Engine for {self._type_of_car} {self.brand} {self.model}')

# # Base Decorator class
# class CarDecorator(Car):
#     def __init__(self, car: Car):
#         self._car = car

# class GPS(CarDecorator):
#     def activate_gps(self):
#         print(f'Activating GPS for {self._car._type_of_car} {self._car._brand} {self._car._model}')

# class Sunroof(CarDecorator):
#     def open_sunroof(self):
#         print(f'Opening Sunroof for {self._car._type_of_car} {self._car._brand} {self._car._model}')

#     def close_sunroof(self):
#         print(f'Closing Sunroof for {self._car._type_of_car} {self._car._brand} {self._car._model}')


# sedan = Sedan('Tata', 'Tigor', 20)
# suv = Sedan('Tata', 'Nexon', 22)

# suv_with_sunroof = Sunroof(suv)
# suv_with_sunroof.start()
# suv_with_sunroof.open_sunroof()
# suv_with_sunroof.close_sunroof()
# # print(f'Mileage for {suv_with_sunroof._brand}', suv_with_sunroof.mileage())
# suv_with_sunroof.stop()


# # Base Car class
# class Car:
#     def __init__(self):
#         self._brand = None
#         self._model = None
#         self._mileage = None
#         self._type_of_car = None

#     @property
#     def mileage(self):
#         return self._mileage

#     @property
#     def model(self):
#         return self._model

#     @property
#     def brand(self):
#         return self._brand

#     def start(self):
#         pass

#     def stop(self):
#         pass


# # Concrete Car classes
# class Sedan(Car):
#     def __init__(self, brand, model, mileage):
#         super().__init__()
#         self._brand = brand
#         self._model = model
#         self._mileage = mileage
#         self._type_of_car = "Sedan"
#         print('Initialized Sedan')

#     def start(self):
#         print(f'Starting Engine for {self._type_of_car} {self.brand} {self.model}')

#     def stop(self):
#         print(f'Stopping Engine for {self._type_of_car} {self.brand} {self.model}')


# class SUV(Car):
#     def __init__(self, brand, model, mileage):
#         super().__init__()
#         self._brand = brand
#         self._model = model
#         self._mileage = mileage
#         self._type_of_car = "SUV"
#         print('Initialized SUV')

#     def start(self):
#         print(f'Starting Engine for {self._type_of_car} {self.brand} {self.model}')

#     def stop(self):
#         print(f'Stopping Engine for {self._type_of_car} {self.brand} {self.model}')


# # Base Decorator class
# class CarDecorator(Car):
#     def __init__(self, car: Car):
#         self._car = car

#     def start(self):
#         self._car.start()

#     def stop(self):
#         self._car.stop()

#     @property
#     def mileage(self):
#         return self._car.mileage

#     @property
#     def model(self):
#         return self._car.model

#     @property
#     def brand(self):
#         return self._car.brand


# # Specific Feature Decorators
# class GPS(CarDecorator):
#     def __init__(self, car):
#         super().__init__(car)

#     def activate_gps(self):
#         print(f'Activating GPS for {self._car.brand} {self._car.model}')

# class Sunroof(CarDecorator):
#     def __init__(self, car):
#         super().__init__(car)

#     def open_sunroof(self):
#         print(f'Opening Sunroof for {self._car.brand} {self._car.model}')

#     def close_sunroof(self):
#         print(f'Closing Sunroof for {self._car.brand} {self._car.model}')


# # Example Usage
# sedan = Sedan('Tata', 'Tigor', 20)
# suv = SUV('Tata', 'Nexon', 22)

# # Add both GPS and Sunroof features
# suv_with_gps = GPS(suv)
# suv_with_gps_and_sunroof = Sunroof(suv_with_gps)

# suv_with_gps_and_sunroof.start()  # Delegates to SUV
# suv_with_gps_and_sunroof.open_sunroof()  # Works because of Sunroof decorator
# suv_with_gps_and_sunroof.close_sunroof()  # Works because of Sunroof decorator
# suv_with_gps_and_sunroof.stop()  # Delegates to SUV

# # Activate GPS
# suv_with_gps_and_sunroof.activate_gps()  # Works because of GPS decorator


# Base Car class
class Car:
    def __init__(self, brand, model, mileage):
        self._brand = brand
        self._model = model
        self._mileage = mileage

    def get_description(self):
        return f"{self._brand} {self._model} with mileage {self._mileage} km/l"

    def cost(self):
        """Base cost for the car"""
        return 0


# Concrete Car classes
class Sedan(Car):
    def __init__(self, brand, model, mileage):
        super().__init__(brand, model, mileage)

    def get_description(self):
        return super().get_description() + " (Sedan)"

    def cost(self):
        return 1000  # Base rental cost for Sedan


class SUV(Car):
    def __init__(self, brand, model, mileage):
        super().__init__(brand, model, mileage)

    def get_description(self):
        return super().get_description() + " (SUV)"

    def cost(self):
        return 1500  # Base rental cost for SUV


# Decorator Base Class
class CarFeatureDecorator(Car):
    def __init__(self, car):
        self._car = car

    def get_description(self):
        return self._car.get_description()

    def cost(self):
        return self._car.cost()


# Specific Feature Decorators
class GPS(CarFeatureDecorator):
    def get_description(self):
        return super().get_description() + ", with GPS"

    def cost(self):
        return super().cost() + 200  # Additional cost for GPS


class Sunroof(CarFeatureDecorator):
    def get_description(self):
        return super().get_description() + ", with Sunroof"

    def cost(self):
        return super().cost() + 300  # Additional cost for Sunroof


class LeatherSeats(CarFeatureDecorator):
    def get_description(self):
        return super().get_description() + ", with Leather Seats"

    def cost(self):
        return super().cost() + 400  # Additional cost for Leather Seats


# Example Usage
if __name__ == "__main__":
    # Create a base car (Sedan)
    sedan = Sedan("Toyota", "Camry", 15)
    print(sedan.get_description(), "-> Cost:", sedan.cost())

    # Add features to the sedan
    sedan_with_gps = GPS(sedan)
    sedan_with_gps_and_sunroof = Sunroof(sedan_with_gps)
    sedan_with_all_features = LeatherSeats(sedan_with_gps_and_sunroof)
    print(sedan_with_all_features.get_description(), "-> Cost:", sedan_with_all_features.cost())

    # Create another car (SUV)
    suv = SUV("Ford", "Explorer", 10)
    print(suv.get_description(), "-> Cost:", suv.cost())

    # Add features to the SUV
    suv_with_sunroof = Sunroof(suv)
    suv_with_all_features = LeatherSeats(GPS(suv_with_sunroof))
    print(suv_with_all_features.get_description(), "-> Cost:", suv_with_all_features.cost())
