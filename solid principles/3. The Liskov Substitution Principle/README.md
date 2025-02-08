# The Liskov Substitution Principle
The Liskov Substitution Principle (L) is the third principle in S.O.L.I.D. It states:

```
Subtypes must be substitutable for their base types without altering the correctness of the program.
```

***In simple terms***: You should be able to replace a parent class with a child class and the program should still work correctly. If a subclass changes the behavior of the base class in unexpected ways, it violates this principle.


## Step-by-Step Explanation
- **Base Class Contract**: A base class defines a "contract" (a set of behaviors that subclasses should follow).
- **Subclasses Should Not Break the Contract**: Subclasses must adhere to the behavior defined by the base class. They shouldn't override methods in a way that changes the expected functionality.


## Understanding When to Apply LSP
- Signs You Need LSP:
    - **Inconsistent Behaviors in Subclasses**: If a subclass cannot fully adhere to the parent class's contract (e.g., save is irrelevant for CSVReport), it’s a sign of LSP violation.
    - **Unnecessary Implementations**: If a subclass needs to override a method only to throw an exception or leave it empty, you likely have an LSP issue.
    - **Surprises in Client Code**: If client code breaks (e.g., process_report), it indicates that subclasses are not substitutable for the base class.


## Theory Behind LSP in Simple Terms
- Liskov Substitution Principle says that a subclass should be replaceable for its base class without altering the correctness of the program.
- If a subclass deviates from the behavior defined by its parent, it leads to bugs and violates LSP.


## Key Takeaways
- When to Apply LSP:
    - If a subclass must override a method to change its behavior significantly or throw an exception.
    - When client code breaks because of an unexpected subclass behavior.
- How to Apply LSP:
    - Refactor your class hierarchy to segregate behaviors (e.g., SavableReport for saving functionality).
    - Use composition or interfaces to encapsulate optional behaviors.
- Benefits of LSP:
    - Avoid surprises in client code.
    - Makes your code easier to maintain and extend.


## Real-World Use Cases
- Payment Gateways:
    - Not all payment processors support refunds. Use LSP to separate processors that handle refunds from those that don’t.
- File Operations:
    - Some file types (e.g., read-only files) don’t support writing. Separate readable and writable behaviors.

