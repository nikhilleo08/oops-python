# Singelton Design Pattern
## Intent
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

![alt text](assets/image.png)

## Problem
The Singleton pattern solves two problems at the same time, violating the Single Responsibility Principle:
- Ensure that a class has just a single instance. Why would anyone want to control how many instances a class has? The most common reason for this is to control access to some shared resource—for example, a database or a file. 
    - Here’s how it works: imagine that you created an object, but after a while decided to create a new one. Instead of receiving a fresh object, you’ll get the one you already created.
    - Note that this behavior is impossible to implement with a regular constructor since a constructor call must always return a new object by design.

![alt text](assets/image-1.png)

2. Provide a global access point to that instance. Remember those global variables that you (all right, me) used to store some essential objects? While they’re very handy, they’re also very unsafe since any code can potentially overwrite the contents of those variables and crash the app.

Just like a global variable, the Singleton pattern lets you access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

There’s another side to this problem: you don’t want the code that solves problem #1 to be scattered all over your program. It’s much better to have it within one class, especially if the rest of your code already depends on it.

Nowadays, the Singleton pattern has become so popular that people may call something a singleton even if it solves just one of the listed problems.


## Solution
All implementations of the Singleton have these two steps in common:

- Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
- Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.

If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.

[Further Read](https://refactoring.guru/design-patterns/singleton)

## Singleton Design Pattern Principles
Below are the principles of the Singleton Pattern:

- **Single Instance**: Singleton ensures that only one instance of the class exists throughout the application.
- **Global Access**: Provide a global point of access to that instance.
- **Lazy or Eager Initialization**: Support creating the instance either when needed (lazy) or when the class is loaded (eager).
- **Thread Safety**: Implement mechanisms to prevent multiple threads from creating separate instances simultaneously.
- **Private Constructor**: Restrict direct instantiation by making the constructor private, forcing the use of the access point

## When to use Singleton Method Design Pattern?
Use the Singleton method Design Pattern when:
- Consider using the Singleton pattern when you need to ensure that only one instance of a class exists in your application.
- Use it when you want to provide a straightforward way for clients to access that instance from a specific location in your code.
- If you think you might want to extend the class later, the Singleton pattern is a good choice. It allows for subclassing, so clients can work with the extended version without changing the original Singleton.
- This pattern is often used in situations like logging, managing connections to hardware or databases, caching data, or handling thread pools, where having just one instance makes sense

## Initialization Types of Singleton
Singleton class can be instantiated by two methods:
- **Early initialization**: In this method, class is initialized whether it is to be used or not. The main advantage of this method is its simplicity. You initiate the class at the time of class loading. Its drawback is that class is always initialized whether it is being used or not.
- **Lazy initialization**: In this method, class in initialized only when it is required. It can save you from instantiating the class when you don’t need it. Generally, lazy initialization is used when we create a singleton class.

## Use Cases for the Singleton Design Pattern
Below are some common situations where the Singleton Design Pattern is useful:

- In applications where creating and managing database connections is resource-heavy, using a Singleton ensures that there’s just one connection maintained throughout the application.
- When global settings need to be accessed by different parts of the application, a Singleton configuration manager provides a single point of access for these settings.
- Singleton helps to centralize control and making it easier to manage the state and actions of user interface components.
- Singleton can effectively organize print jobs and streamlines the process in the systems where document printing is required.

## Applicability
- Use the Singleton pattern when a class in your program should have just a single instance available to all clients; for example, a single database object shared by different parts of the program.
- The Singleton pattern disables all other means of creating objects of a class except for the special creation method. This method either creates a new object or returns an existing one if it has already been created.

- Use the Singleton pattern when you need stricter control over global variables.

- Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.

## How to Implement
- Add a private static field to the class for storing the singleton instance.
- Declare a public static creation method for getting the singleton instance.
- Implement “lazy initialization” inside the static method. It should create a new object on its first call and put it into the static field. The method should always return that instance on all subsequent calls.
- Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects.
- Go over the client code and replace all direct calls to the singleton’s constructor with calls to its static creation method.

## References:
- [GeeksForGeek](https://www.geeksforgeeks.org/singleton-design-pattern/)
- [Refactoring Guru](https://refactoring.guru/design-patterns/singleton)
