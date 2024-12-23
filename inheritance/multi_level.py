# Multilevel Inheritance
# Multilevel inheritance in Python involves creating a chain of classes where each class extends the previous one. In other words, a derived class serves as the base class for another class.

# In this example:

# Animal is the base class, which has a name attribute and a speak method.
# Dog is a derived class from Animal, inheriting its name attribute and speak method. It also has an additional method bark.
# Labrador is a derived class from Dog, inheriting name, speak, and bark. It also has an additional method swim.
# When instances of these classes are created, each class has access to its own methods as well as the methods of its parent classes. The Labrador class, for example, can use methods from both Animal and Dog due to multilevel inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Extends on Animal Base class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")

# Extends on Dog Base class
class Labrador(Dog):
    def swim(self):
        print(f"{self.name} can swim.")

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
labrador = Labrador("Max")

# Calling methods
animal.speak()      # Output: Generic Animal makes a sound.
dog.speak()         # Output: Buddy makes a sound.
dog.bark()          # Output: Buddy barks.
labrador.speak()    # Output: Max makes a sound.
labrador.bark()     # Output: Max barks.
labrador.swim()     # Output: Max can swim.
# dog.swim()        # Error