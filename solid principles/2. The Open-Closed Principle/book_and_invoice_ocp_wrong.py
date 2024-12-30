# Resolved Open-Closed Principle
from abc import ABC, abstractmethod

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
    It contains some fields about invoicing and 1 method:
    - Attributes: 
        - quantity 
        - discount_rate
        - tax_rate
        - total
    - Methods
        - calculate_total method, which calculates the total price
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

class InvoicePrinterBase(ABC):
    @abstractmethod
    def print_invoice(self):
        pass

class ConsoleInvoicePrinter(InvoicePrinterBase):
    """
    ConsoleInvoicePrinter Class is responsible to print the Invoice of the print the invoice to console.
    Methods:
    - print_invoice: 
    """
    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def print_invoice(self):
        print(f"{self.invoice.quantity} x {self.invoice.book.name} ${self.invoice.book.price} = ${self.invoice.book.price * self.invoice.quantity}");
        print("Discount Rate: ", self.invoice.discount_rate);
        print("Tax Rate: ", self.invoice.tax_rate);
        print("Total: ", self.invoice.total);

class InvoicePersistenceBase:
    """
    InvoicePrinter Class is responsible to store the Invoice of the book into a persistence location like DB or File
    """
    @abstractmethod
    def save(self):
        pass

class FileInvoicePersistence(InvoicePersistenceBase):
    def __init__(self):
        super().__init__()
    
    def save(self):
        open('invoice.txt', '+a').write(f"""
{self.invoice.quantity} x {self.invoice.book.name} ${self.invoice.book.price} = ${self.invoice.book.price * self.invoice.quantity}
Discount Rate: {self.invoice.discount_rate}
Tax Rate: {self.invoice.tax_rate}
Total: {self.invoice.total}
""")
        print(f'Invoice for: {self.invoice.book.name} stored in file')


book = Book('The Alchemist', 'Paoulo', 145, 2019, '1234')
alchemist_invoice = Invoice(book, 10, 0.5, 0.15)
alchemist_invoice_printer = ConsoleInvoicePrinter(alchemist_invoice)
alchemist_invoice_printer.print_invoice()

print()

book1 = Book('The Alchemist Part 2', 'Paoulo', 150, 2021, '2345')
alchemist_part_2_invoice = Invoice(book1, 100, 0.05, 0.20)
alchemist_part_2_invoice_printer = ConsoleInvoicePrinter(alchemist_part_2_invoice)
alchemist_part_2_invoice_printer.print_invoice()

print()

invoice_saver = FileInvoicePersistence(alchemist_invoice)
invoice_saver1 = FileInvoicePersistence(alchemist_part_2_invoice)
invoice_saver.save_to_file()
invoice_saver1.save_to_file()

# How does this Refactored code Solves OCP

# Extensibility for Printing: To add a new printing format (e.g., JSONInvoicePrinter), you create a new class implementing InvoicePrinterBase without modifying the existing ConsoleInvoicePrinter.

# Extensibility for Persistence: To add a new persistence method (e.g., CloudStoragePersistence), you create a new class implementing InvoicePersistenceBase without modifying the existing FileInvoicePersistence.

# This approach ensures that the existing code remains unchanged when new functionality is added, adhering to the Open-Closed Principle.