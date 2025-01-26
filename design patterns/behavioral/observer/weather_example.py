# Observer interface
class Observer:
    def update(self, temperature):
        raise NotImplementedError("Subclass must implement abstract method")


# Subject (Publisher) interface
class Subject:
    def add_observer(self, observer):
        raise NotImplementedError("Subclass must implement abstract method")

    def remove_observer(self, observer):
        raise NotImplementedError("Subclass must implement abstract method")

    def notify_observers(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Concrete Subject (Weather Station)
class WeatherStation(Subject):
    def __init__(self):
        self.observers = []  # List of observers
        self.temperature = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        print(f"WeatherStation: Temperature updated to {temperature}°C.")
        self.temperature = temperature
        self.notify_observers()  # Notify all observers of the change

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)


# Concrete Observer 1 (Phone Display)
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: Received temperature update: {temperature}°C.")


# Concrete Observer 2 (LCD Display)
class LCDDisplay(Observer):
    def update(self, temperature):
        print(f"LCDDisplay: Temperature displayed on LCD: {temperature}°C.")


# Client Code
if __name__ == "__main__":
    # Create the subject
    weather_station = WeatherStation()

    # Create observers
    phone_display = PhoneDisplay()
    lcd_display = LCDDisplay()

    # Add observers to the subject
    weather_station.add_observer(phone_display)
    weather_station.add_observer(lcd_display)

    # Change temperature
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    # Remove an observer and update again
    weather_station.remove_observer(phone_display)
    weather_station.set_temperature(20)
