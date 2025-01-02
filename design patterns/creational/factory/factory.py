from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Delivering by road using a Truck."

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea using a Ship."


class TransportFactory:
    @staticmethod
    def get_transport(mode: str) -> Transport:
        if mode == "road":
            return Truck()
        elif mode == "sea":
            return Ship()
        else:
            raise ValueError("Invalid transport mode")


if __name__ == "__main__":
    mode = input("Enter transport mode (road/sea): ").strip().lower()
    try:
        transport = TransportFactory.get_transport(mode)
        print(transport.deliver())
    except ValueError as e:
        print(e)
