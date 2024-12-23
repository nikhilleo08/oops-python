# Hierarchical inheritance
# In hierarchical inheritance, a single base class (parent class) is inherited by multiple derived classes (child classes). Each derived class shares common attributes and methods from the base class but may have its own additional attributes and methods.

# In this example:

# Animal is the base class with a constructor (__init__) and a method speak.
# Dog, Cat, and Bird are derived classes that inherit from the Animal class.
# Each derived class has its own implementation of the speak method, providing a unique behavior for each type of animal.
# With hierarchical inheritance, you can add more derived classes as needed, each inheriting from the common base class. This structure promotes code reuse and organization, as shared functionality is centralized in the base class, and specific behaviors can be defined in the derived classes.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Hello!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} sings beautifully!"

class Elephant(Animal):
    pass

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")
elephant = Elephant("Homey")

# Calling the speak method on each object
print(dog.speak())   # Output: Buddy says Woof!
print(cat.speak())   # Output: Whiskers says Meow!
print(bird.speak())  # Output: Tweetie sings beautifully!
print(elephant.speak())  # Output: Tweetie sings beautifully!