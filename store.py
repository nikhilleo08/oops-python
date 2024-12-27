# Blueprint
class Item:
    # Methods with __ are called Magic Methods
    # Parameterized constructor to initialize the object with values passed in parameters
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    # Methods for class
    # Python passes the object itself as the first argument when we call 
    # the methods so we use self to denote the object on which the method is called
    def calculate_total_price(self):
        return self.qty * self.price

# Creating a new Object of class Item
item1 = Item("iPhone", 80, 1199)

# Assigning values to the object attributes
# item1.name = "Phone"
# item1.qty = 5
# item1.price = 100

print(type(item1)) # class Item
print(type(item1.name)) # class str
print(type(item1.qty)) # class int
print(type(item1.price)) # class int
print(item1.calculate_total_price()) # Returns qty * price
