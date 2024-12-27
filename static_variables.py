# Best Practices for Using Class Variables
# Use Class Variables for Shared Data: If you want all instances to share a particular value or state, use class variables.
# Modify Class Variables via Class Name: Always modify class variables using the class name (ClassName.variable) to avoid unintentionally creating an instance-level copy.
# Avoid Modifying Class Variables from Instances: Modifying class variables through instances can lead to confusion, as it creates instance-level variables.
# Be Careful in Multithreaded Environments: In multithreaded programs, unsynchronized class variables can cause race conditions.

# Instance Variables vs Class Variables in Python
# Instance Variables: Variables that are unique to each object. They are created inside methods (typically __init__()).
# Class Variables (Static Variables): Variables shared among all instances of a class. They are defined within the class, outside any methods.

class MyClass:
    static_var = 0  # Class variable

    def __init__(self):
        MyClass.static_var += 1  # Modify through class name
        self.instance_var = MyClass.static_var  # Instance variable

obj1 = MyClass()
print("obj1.instance_var:", obj1.instance_var)  # Output: 1

obj2 = MyClass()
print("obj2.instance_var:", obj2.instance_var)  # Output: 2

# Access class variable directly
print("MyClass.static_var:", MyClass.static_var)  # Output: 2

# Modify class variable using obj1 (this creates a new instance variable)
obj1.static_var = 10
print("obj1.static_var:", obj1.static_var)  # Output: 10 (instance variable now)
print("MyClass.static_var:", MyClass.static_var)  # Output: 2 (unchanged)
print("obj2.static_var:", obj2.static_var)  # Output: 2 (unchanged)

# Key Differences Between Class Variables in Python and Static Variables in Java/C++

# While class variables in Python and static variables in Java/C++ serve a similar purpose of being shared across all instances, they behave differently when modified through an instance:

# Java/C++ Behavior: When you modify a static variable in Java or C++, the change is reflected across all instances of the class, and they all remain synchronized with the static variable’s value.

# Python Behavior: In Python, if you modify a class variable through an instance, a new instance variable is created. This separates the modified value from the original class variable, which remains unchanged for other instances.

# Features of Static Variables
# Memory Efficiency: Static variables are allocated memory once when the object for the class is created for the first time.
# Class Scope: Static variables are created outside methods but inside the class.
# Access Through Class: Static variables can be accessed through the class but not directly through an instance.
# Consistent Behavior: The behavior of static variables doesn’t change for every object.
