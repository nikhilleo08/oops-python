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

my_animal = Animal()
animal1 = Dog()
animal2 = Cat()

my_animal.make_sound()  # Calls the make_sound method of the Animal class
animal1.make_sound()  # Calls Dog's make_sound method
animal2.make_sound()  # Calls Cat's make_sound method


# Dynamic Method Dispatch
# Dynamic method dispatch, also known as runtime polymorphism, is a feature in Python that allows you to invoke a method on an object, and the method that gets executed is determined at runtime based on the actual type of the object. This enables you to create more flexible and extensible code by using inheritance and method overriding.

# Here's how dynamic method dispatch works in Python:

# Inheritance: Dynamic method dispatch relies on inheritance. You have a super class (base class) and one or more subclasses (derived classes) that inherit from the super class.

# Method Overriding: To achieve dynamic method dispatch, you must override a method in a subclass. In other words, you define a method with the same name and parameters as the method in the superclass.

# Polymorphism: The superclass reference can be used to refer to an object of any subclass. This is possible due to polymorphism. For example, if you have a superclass reference, you can use it to refer to objects of either the superclass or any of its subclasses.

# In this example, we have a superclass Animal with a method makeSound, and two subclasses Dog and Cat that override the makeSound method. We can create objects of Dog and Cat and assign them to a reference of the Animal class. When we call makeSound on these references, the specific implementation of makeSound in the respective subclass is invoked at runtime. This is dynamic method dispatch in action.

# Dynamic method dispatch allows you to write more generic code that can work with objects of different subclasses, promoting code reusability and flexibility in your Python programs.

