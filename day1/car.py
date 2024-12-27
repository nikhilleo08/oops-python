from enum import Enum

class EngineType(Enum):
    PETROL = "petrol" 
    DIESEL = "diesel"

class Car:
    def __init__(
        self, 
        brand: str, 
        model: str, 
        transmission: str, 
        price: float, 
        colour: str,
        engine_type: EngineType,
        mileage: float = 0.0,    
        year: int = 2024,
        fuel_capacity: float = 40.0,
    ):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.transmission = transmission
        self.colour = colour
        self.engine_type = engine_type
        self._fuel_capacity = fuel_capacity  # Protected
        self._kms_driven = 0  # Protected
        self.__seating_capacity = 5 # Private
        self.__number_of_doors = 4 # Private
        self.__gps_enabled = True # Private
        self.__current_fuel_level = 1.0  # Private
        self.__is_parked = True  # Private
        self.__current_speed = 0  # Private
        self.__max_speed = 170 # Private

    @property
    def current_speed(self):
        return self.__current_speed

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def current_fuel_level(self):
        return self.__current_fuel_level

    def __set_current_speed(self, val):
        self.__current_speed = val

    def describe_features_and_current_state(self):
        print(f"""
Brand: {self.brand}
Model: {self.model}
colour: {self.colour}
Transmission: {self.transmission}
Year of Man: {self.year}
Engine Type: {self.engine_type}
KMs Driven: {self._kms_driven}
Is Parked: {self.__is_parked}
Current Speed: {self.current_speed}
Current Fuel Level: {self.current_fuel_level}
""")
    
    def start_engine(self):
        self.__is_parked = False
        print(f'Starting {self.brand} {self.model}')
    
    def stop_engine(self):
        self.__is_parked = True
        print(f'Stopping {self.brand} {self.model}')
    
    def drive(self):
        print(f'Drive mode for {self.brand} {self.model}')
    
    def drive_complete(self, kms_driven: float):
        self._kms_driven += kms_driven
        self.__current_fuel_level -= round(kms_driven/self.mileage, 2)
        self.__set_current_speed(0)
        self.stop_engine()
        self.open_door()
        self.close_door()

    def park(self):
        print(f'Parking {self.brand} {self.model}')

    def open_door(self):
        print(f'Opening {self.brand} {self.model} door')

    def close_door(self):
        print(f'Closing {self.brand} {self.model} door')

    def accelerate(self, speed: int):
        if not self.__is_parked:
            if speed > 0 and self.current_speed + speed <= self.max_speed:
                self.__set_current_speed(self.current_speed + speed)
                print(f"Accelerating... Current speed: {self.current_speed} km/h.")
            elif speed < 0 and self.current_speed + speed >= 0:
                self.__set_current_speed(self.current_speed + speed)
                print(f"Deaccelerating... Current speed: {self.current_speed} km/h.")
            else:
                print(f"Cannot {'accelerate' if speed > 0 else 'deaccelerate'}. Ensure the car is within speed limits.")
        else:
            print("Cannot accelerate. Ensure the car is not parked.")

    def refuel(self, amount: float):
        if self.__is_parked and self.__current_fuel_level < self._fuel_capacity:
            self.__current_fuel_level += amount
            print(f"Refilling {self.engine_type.value.title()}... Current fuel capacity: {self.__current_fuel_level} ltrs.")
        else:
            print("Cannot refill fuel. Ensure the car is parked and within current fuel capacity is less than maximum fuel capacity.")


tata_punch = Car('Tata', 'Punch Adventure', 'Manual', '10,00,000', 'White', EngineType.PETROL, 22, 2024)
tata_punch.refuel(20)
tata_punch.open_door()
tata_punch.start_engine()
tata_punch.drive()
tata_punch.accelerate(10)
tata_punch.accelerate(10)
tata_punch.accelerate(10)
tata_punch.accelerate(10)
tata_punch.accelerate(100)
tata_punch.accelerate(50)
tata_punch.accelerate(-50)
tata_punch.accelerate(-50)
tata_punch.accelerate(-50)
tata_punch.refuel(10)
tata_punch.describe_features_and_current_state()
tata_punch.drive_complete(100.7)
tata_punch.refuel(10)
tata_punch.describe_features_and_current_state()
