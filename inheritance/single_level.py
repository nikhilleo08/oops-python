# Single Inheritance
# Single inheritance is a type of inheritance in object-oriented programming where a class inherits from only one base class. In Python, you can achieve single inheritance using a straightforward syntax.

# Explanation:

# Animal is the base class with a constructor __init__ and a method speak.
# Dog is the derived class that inherits from the Animal class using the syntax class Dog(Animal):.
# The Dog class has its own implementation of the speak method, which overrides the method in the base class.
# An instance of the Dog class, named Buddy, is created.
# When calling the speak method on the dog_instance, it invokes the overridden method in the Dog class.
# In this example, the Dog class inherits from the Animal class, and it can use and override the methods of the base class. Single inheritance is simple and often sufficient for many scenarios, promoting a clean and straightforward class hierarchy.

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the derived class
dog_instance = Dog("Buddy")

# Calling methods from the base and derived classes
dog_instance.speak()  # This will call the overridden method in Dog class