class Book:
    """
    This is a simple book class with some fields. Nothing fancy. I am not making fields private so that we don't need to deal with getters and setters and can focus on the logic instead.
    """
    def __init__(self, name: str, author: str, price: int, year: int, isbn: str):
        self.name = name
        self.author = author
        self.price = price
        self.year = year
        self.isbn = isbn

class Invoice:
    """
    Invoice class which will contain the logic for creating the invoice and calculating the total price.
    It contains some fields about invoicing and 3 methods:
    - Attributes: 
        - quantity 
        - discount_rate
        - tax_rate
        - total
    - Methods
        - calculate_total method, which calculates the total price.
        - print_invoice method, that should print the invoice to console.
        - save_to_file method, responsible for writing the invoice to a file.
    """
    def __init__(self, book: Book, quantity: int, discount_rate: float, tax_rate: float):
        self.book = book
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.total = self.calculate_total()
    
    def calculate_total(self):
        price = (self.book.price - (self.book.price * self.discount_rate)) * self.quantity
        total_price = price * (1 + self.tax_rate)
        return round(total_price, 2)

    def print_invoice(self):
        print(f"{self.quantity} x {self.book.name} ${self.book.price} = ${self.book.price * self.quantity}");
        print("Discount Rate: ", self.discount_rate);
        print("Tax Rate: ", self.tax_rate);
        print("Total: ", self.total);

    def save_to_file(self):
        pass


book = Book('The Alchemist', 'Paoulo', 145, 2019, '1234')

alchemist_invoice = Invoice(book, 10, 0.5, 0.15)
alchemist_invoice.print_invoice()

# Our class violates the Single Responsibility Principle in multiple ways.

# The first violation is the printInvoice method, which contains our printing logic. The SRP states that our class should only have a single reason to change, and that reason should be a change in the invoice calculation for our class.

# But in this architecture, if we wanted to change the printing format, we would need to change the class. This is why we should not have printing logic mixed with business logic in the same class.

# There is another method that violates the SRP in our class: the saveToFile method. It is also an extremely common mistake to mix persistence logic with business logic.

# Don't just think in terms of writing to a file – it could be saving to a database, making an API call, or other stuff related to persistence.

# FIX for the following class

# We can create new classes for our printing and persistence logic so we will no longer need to modify the invoice class for those purposes.

# We create 2 classes, InvoicePrinter and InvoicePersistence, and move the methods.
