# Strategy Design Pattern
The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. This allows the algorithm to vary independently from the clients that use it.

Overview
- **Intent**: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently of clients that use it.
- **Problem**: When a class has multiple ways to perform a task (e.g., sorting, payment processing) leading to conditional statements (e.g., if/else, switch), making the code rigid and hard to maintain.
- **Solution**: Decouple algorithms into separate classes (strategies) and allow runtime selection.

## Real-World Analogy
Think about a payment system for an e-commerce application. The system supports different payment methods: credit card, PayPal, and cryptocurrency. Depending on the user’s choice, the appropriate payment strategy is selected at runtime. The core system does not need to change whenever a new payment method is added—new strategies are simply plugged in.


## Core Components
- **Strategy Interface**: Declares the method(s) all concrete strategies must implement.
- **Concrete Strategies**: Implement the algorithm defined in the interface.
- **Context**:
    - Holds a reference to a strategy object.
    - Delegates the work to the strategy (composition over inheritance).
    - May provide an interface for clients to switch strategies

## Key Concepts of the Strategy Pattern
- **Composition over Inheritance**: Strategies are injected into the context, avoiding subclass bloat.
- **Open/Closed Principle**: New strategies can be added without modifying existing code.
- **Runtime Flexibility**: Algorithms can be swapped dynamically (e.g., changing compression strategies in a file utility)

## Benefits vs. Drawbacks
|Benefits |	Drawbacks |
|---------|-----------|
|Eliminates conditional logic |	Increased number of classes |
|Promotes code reuse and modularity	| Clients must understand strategies|
|Easy to test and mock strategies | Overkill for simple algorithms|

## Comparison with Similar Patterns
- **State Pattern**: Strategies are independent and unaware of each other, while states transition between each other.
- **Template Method**: Uses inheritance to define a skeleton algorithm, while Strategy uses composition for full algorithm replacement.

## Advanced Considerations
- **Stateless Strategies**: Strategies can be shared across contexts if they don’t hold state (e.g., thread-safe).
- **Dependency Injection**: Strategies are often injected via constructors or setters for loose coupling.
- **Parameter Passing**: Context passes all necessary data to the strategy method (e.g., pay(amount)).

## Questions for Deeper Understanding
### Q1: When is the Strategy Pattern most appropriate?
### Answer: 
- When:
    - Multiple variants of an algorithm exist.
    - Conditional statements are used to select algorithms.
    - Algorithms need to be swapped at runtime (e.g., user selects a payment method).

##  Q2: How does Strategy differ from the Factory Pattern?
### Answer:
- Factory creates objects, while Strategy encapsulates algorithms.
- Factory focuses on object creation, Strategy on behavior delegation.

## Q3: How would you handle strategy instantiation in a multithreaded environment?
### Answer:
- Use stateless strategies (no instance variables).
- Synchronize strategy methods if they access shared resources.
- Create a new strategy instance per thread if stateful.

## Q4: What happens if a strategy needs data from the Context?
### Answer: 
- Pass the data as parameters to the strategy’s method. Avoid coupling the strategy to the Context’s internal state.

## Q5: Why is Strategy better than inheritance for algorithm variation?
### Answer: 
- Inheritance creates rigid class hierarchies (e.g., Duck with fly() method forces all subclasses to inherit flying behavior). Strategy allows dynamic behavior changes without subclassing.

## Q6: What SOLID principles does the Strategy Pattern align with?
### Answer:
- **Single Responsibility**: Each strategy handles one algorithm.
- **Open/Closed**: New strategies can be added without modifying existing code.
- **Dependency Inversion**: Context depends on abstractions (interfaces), not concrete strategies.


## Q7: How would you unit test a Context class?
## Answer:
- Mock the strategy interface.
- Verify the context calls the strategy method with correct parameters.

## Q8: Can a strategy hold a reference to the Context? Is this advisable?
### Answer: 
- Yes, but it creates tight coupling. Prefer passing data via method parameters instead.

## Q9: When would you avoid the Strategy Pattern?
### Answer:
- If only one algorithm is needed.
- If conditional logic is simple (e.g., a single if/else).
- If performance is critical (method calls add overhead).

## Q10: How do I decide whether to use classes or functions for strategies?
### Answer
- Use classes if:
    - Strategies require maintaining internal state.
    - You need the flexibility to add behaviors or extend logic easily.
- Use functions if:
    - Strategies are stateless and consist of simple logic

## Real-World Applications
- **Sorting Algorithms**: Selecting between quicksort, mergesort, or bubblesort at runtime.
- **Compression Algorithms**: Choosing between ZIP, RAR, or GZIP for file compression.
- **Authentication Systems**: Switching between OAuth, SAML, or custom authentication logic.

## Advantages of the Strategy Pattern
- **Open/Closed Principle**: Adding a new strategy does not require modifying existing code.
- **Runtime Flexibility**: Strategies can be selected or swapped dynamically at runtime.
- **Encapsulation of Behavior**: Each strategy encapsulates a specific behavior, making the code easier to maintain.

## Disadvantages
- **Increased Complexity**: Introducing too many strategies can lead to more classes.
- **Overhead**: If the algorithms are simple, using the Strategy Pattern may be overkill.