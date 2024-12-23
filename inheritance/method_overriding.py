# Method Overriding with Single Inheritance
# Method overriding in Python is a mechanism that allows a subclass to provide a specific implementation for a method that is already defined in its superclass. The overriding method in the subclass should have the same name and parameters (if overridden), but it may provide a different implementation.

# This code demonstrates method overriding in Python. Here's an explanation of how it works:

# Base class Animal: This is the base class that defines a method make_sound(). The implementation of this method prints "Animal makes a sound".

# Subclass Dog and Cat: These are subclasses of Animal. Each subclass defines its own version of the make_sound() method, which overrides the implementation in the base class. The Dog subclass defines make_sound() to print "Dog barks", and the Cat subclass defines make_sound() to print "Cat meows".

# Object Creation:

# animal1 is created as an instance of the Dog class.
# animal2 is created as an instance of the Cat class.
# Method Call:

# When animal1.make_sound() is called, it invokes the make_sound() method of the Dog class because animal1 is an instance of Dog. This demonstrates dynamic polymorphism, where the method to be called is determined at runtime based on the type of the object.
# Similarly, when animal2.make_sound() is called, it invokes the make_sound() method of the Cat class because animal2 is an instance of Cat.

# Base class
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

# Subclass 1
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

# Subclass 2
class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

animal1 = Dog()
animal2 = Cat()

animal1.make_sound()  # Calls Dog's make_sound method
animal2.make_sound()  # Calls Cat's make_sound method
