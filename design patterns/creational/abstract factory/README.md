# Abstract Factory Design Pattern
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

It helps in building systems where objects need to be created in a consistent manner without coupling the client code to specific implementations.


# Real-World Analogy
**Example**: Furniture Factory (Modern vs. Victorian Style)
Imagine you own a furniture company that produces Modern and Victorian-style furniture.

Each style has different Chair, Sofa, and Table designs. Instead of allowing customers to pick furniture randomly, you want to ensure they buy matching furniture (all modern or all Victorian).

The Abstract Factory allows you to define a factory interface (FurnitureFactory) that can produce related furniture items (Chair, Sofa, Table) while ensuring that only one style is chosen at a time (Modern or Victorian).

# Intent of the Abstract Factory Pattern
- ✔ Encapsulates object creation without exposing details.
- ✔ Ensures compatibility between related objects.
- ✔ Decouples client code from specific concrete classes.

## Problem Statement
You need to build a cross-platform UI toolkit that supports multiple operating systems like Windows and Mac.

Each OS has its own style of buttons and checkboxes.

A naive approach would be:
```python
if os_type == "Windows":
    button = WindowsButton()
elif os_type == "Mac":
    button = MacButton()
```
This approach violates the Open-Closed Principle and makes adding new platforms difficult.

## Solution: Using the Abstract Factory Pattern
Instead of using if-else statements, we define:
- **Abstract Factory (GUIFactory)**: Creates related UI components.
- **Concrete Factories (WindowsFactory, MacFactory)**: Implement platform-specific UI creation.
- **Abstract Products (Button, Checkbox)**: Define the interfaces for UI components.
- **Concrete Products (WindowsButton, MacButton, etc.)**: Implement the UI for specific OS.
- **Client Code**: Uses the factory without knowing the exact class names.

## Key Participants
- **Abstract Factory (GUIFactory)**:
    - Declares methods for creating abstract products (create_button(), create_checkbox()).
- **Concrete Factories (WindowsFactory, MacFactory)**:
    - Implements the factory interface to create platform-specific components.
- **Abstract Product (Button, Checkbox)**:
    - Defines a common interface for products.
- **Concrete Product (WindowsButton, MacButton, WindowsCheckbox, MacCheckbox)**:
    - Implements the actual UI components for each platform.
- **Client Code**
    - Uses the factory but does not depend on specific classes.

## Key Points in Code
- Abstract Factory (**GUIFactory**) defines the structure for UI factories.
- Concrete Factories (**WindowsFactory, MacFactory**) implement platform-specific object creation.
- Abstract Products (**Button, Checkbox**) define the UI components.
- Concrete Products (**WindowsButton, MacButton, etc.**) implement platform-specific UI elements.
- Client Code (**get_factory()**) dynamically selects the appropriate factory without modifying existing code.

## Real-World Use Cases
- ✅ Cross-Platform UI Libraries:
    - GUI frameworks like Qt, Java Swing, Tkinter use this pattern.
- ✅ Game Development:
    - Used in Unreal Engine, Unity to create platform-specific UI.
- ✅ Database Connection Factories:
    - Abstracting SQL vs NoSQL database connections.
- ✅ Theming Systems:
    - Dark mode vs Light mode UI systems.
- ✅ Cloud Storage APIs:
    - Providing APIs for AWS S3, Google Cloud Storage, and Azure Blob Storage.


## Advantages
- ✔ Ensures Consistency: Related objects are created together.
- ✔ Encapsulates Object Creation: Reduces coupling between components.
- ✔ Easier Maintenance: New product families can be added easily.

## Disadvantages
- ❌ **Increases Complexity**: More classes and interfaces to manage.
- ❌ **Difficult to Modify Single Products**: Changing just one product in a family may require modifying multiple factories.

## Questions for Deeper Understanding
### Q1: How is Abstract Factory different from Factory Method?
- Factory Method: Creates a single type of product.
- Abstract Factory: Creates a family of related products.
### Q2: How can we add a new OS like Linux?
- Simply create a new LinuxFactory and define LinuxButton and LinuxCheckbox.
### Q3: How do we reduce the complexity of the Abstract Factory Pattern?
- Use the Prototype Pattern to create objects dynamically instead of having multiple concrete factories.
### Q4: How does Abstract Factory improve scalability?
- Without Abstract Factory, adding Mac UI support would require multiple if-else conditions in client code.
- With Abstract Factory, adding Mac UI is just creating a new MacFactory without modifying client code.
- 👉 This follows the Open/Closed Principle (OCP) → Open for extension, Closed for modification.
### Q5: What happens if we need a new UI component (e.g., Menu)?
We need to modify the abstract factory interface to include create_menu().
```python
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_menu(self) -> Menu:  # New product
        pass
```
Then, each concrete factory (WindowsFactory, MacFactory) must implement create_menu().

👉 This follows Liskov Substitution Principle (LSP) → Derived classes must implement all behaviors of the base class.


## Add another OS type dynamically
To add another OS type dynamically, you can modify the get_factory function to accept and register new factories dynamically instead of hardcoding them in a dictionary.

## Solution: Use a Global Registry for Factories
A global dictionary can be used to store and dynamically register new factory classes.

## Explanation:
- **Global _factory_registry Dictionary**
    - Stores all available OS factories dynamically
    - Initially contains "windows" and "mac".
- **register_factory(os_type, factory_class) Function**
    - Allows adding new OS types dynamically.
    - Ensures that only subclasses of GUIFactory can be registered.
- **get_factory(os_type) Function**
    - Fetches the factory dynamically from _factory_registry.
    - Defaults to "windows" if the requested OS type is not found.
- **Dynamically Registering LinuxFactory**
    - We create new LinuxButton, LinuxCheckBox, and LinuxFactory classes.
    - We register LinuxFactory dynamically with register_factory("linux", LinuxFactory).
    - Now, calling get_factory('linux') returns the correct factory.

This approach allows you to add new OS types dynamically without modifying existing code, making it more flexible and scalable. 🚀


## 🛠 Thought Process for Designing an Abstract Factory
### What are the Products?
- Primary Product: Notification (Email, SMS, Push)
- Secondary Product: Logging Service (AWSLoggingService, AzureLoggingService)
### What Should the Abstract Factory Do?
- Must be extendable without modifying existing code.
- Should support multiple notification types.
### How Should Factories Be Structured?
- Concrete Factories (AWS, Azure) must implement a common interface.
- Use registration-based approach to avoid modifying existing code.

## 🚀 Summary
|Approach   	|Pros   	|Cons   	|
|:---	|:---	|:---	|
|Original Factory (Hardcoded Email)|Simple|Violates OCP, no extensibility|
|Factory Method with Parameters	|Dynamic object creation|Needs manual updates for new types|
|Separate Factories (Email, SMS, Push)|Strict separation|Too many classes|
|Abstract Factory + Registration-based Factory ✅|Fully extensible, runtime registration|More setup|

### ✔ Best Approach → Abstract Factory + Registration-based Factory 💡
- New notifications can be registered at runtime.
- Different cloud providers (AWS, Azure) can have their own factories.
- Logging is decoupled for flexibility.

## 📌 Final Thought
    💡 When should you use an Abstract Factory?
    👉 When you need to create multiple related objects (Email, SMS, Push) and different implementations (AWS, Azure) without modifying existing code.


## 💡 Why Separate Concrete Product Classes?
### 1️⃣ Different Responsibilities Should Be Separate (Single Responsibility Principle)
- We are following good software design principles (especially SRP - Single Responsibility Principle).
    - PaymentProcessor is responsible for processing payments.
    - PaymentValidator is responsible for validating payments.
- 💡 Why keep them separate?
    - If tomorrow, PayPal decides to use a third-party validator (e.g., Visa Secure), we don’t need to modify the PayPal processing logic.
    - If Stripe changes its processing logic but keeps validation the same, we don’t need to modify validation code.

### 2️⃣ Flexibility: Easily Swap Implementations
- By keeping them separate, we gain flexibility.

- 🚀 Example:
Imagine that PayPal decides to outsource validation to a third-party service, but still handles payment processing internally.

### 3️⃣ Scalability: Add New Functionalities Easily
- If tomorrow we need a new feature (e.g., Fraud Detection Validator), we don’t need to change existing processors.
- Instead, we can extend our validation logic:
```python
class FraudDetectionValidator(PaymentValidator):
    def validate(self, card_number: str, amount: float) -> bool:
        print(f"Running fraud detection on card {card_number} for ${amount}")
        return True  # Assume validation succeeds
```
Now, Stripe can use this without modifying StripeProcessor:
```python
class StripeFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return StripeProcessor()

    def create_validator(self) -> PaymentValidator:
        return FraudDetectionValidator()  # Stripe now uses fraud detection!
```
💡 If Processor & Validator were in the same class, this would be much harder to manage!

### 4️⃣ Following the Abstract Factory Pattern Correctly
- The Abstract Factory Pattern is about creating families of related objects.
- 👎 Incorrect Approach (Combining Processing & Validation)

```python
class PayPal(PaymentProcessor, PaymentValidator):  # ❌ Mixing Responsibilities
    def process(self, amount): ...
    def validate(self, card_number, amount): ...
```
This breaks the Single Responsibility Principle and makes it harder to change one part without affecting the other.

#### ✅ Correct Approach (Separate Products)

```python
class PayPalProcessor(PaymentProcessor):  # ✅ Only processes payments
    def process(self, amount): ...

class PayPalValidator(PaymentValidator):  # ✅ Only validates payments
    def validate(self, card_number, amount): ...
```

#### 💡 Why?
- This follows the Abstract Factory Pattern correctly.
- We can swap or extend validators/processors easily.
- If we introduce a new validator (like AI Fraud Detection), we don’t touch existing processors.

## 🎯 Final Thoughts:
- ✅ Separation makes the system flexible, scalable, and maintainable.
- ✅ You can swap different implementations without modifying existing code.
- ✅ It follows SOLID principles (especially SRP & OCP).
- ✅ You can introduce new validators/processors in the future without breaking the existing system.

So, by creating separate concrete products, we make the system more robust, scalable, and future-proof! 🚀💡


