# Multiple Inheritance
# Multiple inheritance in Python allows a class to inherit attributes and methods from more than one base class. This means that a derived class can inherit from two or more parent classes. The syntax for multiple inheritance is as follows:

# class DerivedClass(BaseClass1, BaseClass2):
#     # Attributes and methods of DerivedClass

# In this example, Bird and Bat are both derived classes that inherit from both Animal and Flyer. The speak method is overridden in both derived classes, and they inherit the fly method from the Flyer class.

# Keep in mind that while multiple inheritance can be powerful, it also requires careful design to avoid potential issues such as the diamond problem (a situation where ambiguity arises if two base classes have a common ancestor). It's essential to use multiple inheritance judiciously and consider alternative design patterns when appropriate.

