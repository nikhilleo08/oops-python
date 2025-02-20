# SOLID Principles
## The Single Responsibility Principle
- The Single Responsibility Principle states that a class should do one thing and therefore it should have only a single reason to change.

- To state this principle more technically: Only one potential change (database logic, logging logic, and so on.) in the software’s specification should be able to affect the specification of the class.

- This means that if a class is a data container, like a Book class or a Student class, and it has some fields regarding that entity, it should change only when we change the data model.

- Following the Single Responsibility Principle is important. First of all, because many different teams can work on the same project and edit the same class for different reasons, this could lead to incompatible modules.

- Second, it makes version control easier. For example, say we have a persistence class that handles database operations, and we see a change in that file in the GitHub commits. By following the SRP, we will know that it is related to storage or database-related stuff.

- Merge conflicts are another example. They appear when different teams change the same file. But if the SRP is followed, fewer conflicts will appear – files will have a single reason to change, and conflicts that do exist will be easier to resolve.


## The Open-Closed Principle
- The Open-Closed Principle requires that classes should be open for extension and closed to modification.

- Modification means changing the code of an existing class, and extension means adding new functionality.

- So what this principle wants to say is: We should be able to add new functionality without touching the existing code for the class. This is because whenever we modify the existing code, we are taking the risk of creating potential bugs. So we should avoid touching the tested and reliable (mostly) production code if possible.

- But how are we going to add new functionality without touching the class, you may ask. It is usually done with the help of interfaces and abstract classes.


## The Liskov Substitution Principle
## The Interface Segregation Principle
## The Dependency Inversion Principle
