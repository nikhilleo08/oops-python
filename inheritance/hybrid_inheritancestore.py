# Hybrid Inheritance
# Hybrid inheritance in Python is a combination of multiple and hierarchical inheritance. In this scenario, two or more classes are derived from a single base class using hierarchical inheritance, and then a new class is derived from these subclasses using multiple inheritance.

# Let's illustrate this concept with an example:

# Animal is the base class with a basic speak method.
# Mammal and Bird are subclasses that inherit from Animal using hierarchical inheritance. They add specific methods related to mammals and birds, respectively.
# Platypus is a derived class that inherits from both Mammal and Bird using multiple inheritance. It combines characteristics of both mammals and birds.
# When you create an object of the Platypus class (platypus_obj), it can access methods from both Mammal and Bird, as well as override or provide its own implementation of the speak method. This demonstrates the combination of multiple and hierarchical inheritance, forming a hybrid inheritance structure.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclasses using hierarchical inheritance
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} is giving birth to live young."

class Bird(Animal):
    def lay_eggs(self):
        return f"{self.name} is laying eggs."

# Derived class using multiple inheritance
class Platypus(Mammal, Bird):
    def speak(self):
        return f"{self.name} says Quack!"

# Example usage
platypus_obj = Platypus("Perry")

print(platypus_obj.speak())        # Output: Perry says Quack!
print(platypus_obj.give_birth())   # Output: Perry is giving birth to live young.
print(platypus_obj.lay_eggs())     # Output: Perry is laying eggs.