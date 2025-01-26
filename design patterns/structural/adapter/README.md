# Adapter Pattern
The Adapter pattern allows two incompatible interfaces to communicate with each other. It provides a wrapper (adapter) that translates one interface to another. This is useful when you have existing code that needs to be integrated with another system that has a different interface.

## When to Use the Adapter Pattern?
- When you want to use an existing class, but its interface doesn't match the one you need.
- When you have classes that can't be modified directly (e.g., third-party libraries).
- When you want to make multiple incompatible interfaces compatible.
- **Legacy Code**: When you need to integrate a new system with an old system but can't modify the old system’s code (e.g., integrating a new payment gateway with an older system).
- **Third-Party Libraries**: When using a third-party library that has an interface incompatible with your system.
- **Standardization**: When you have different systems with different interfaces but need a common way of interacting with them.


## Components in the Adapter Pattern:
- **Target**: The interface that clients expect.
- **Adaptee**: The existing class whose interface is incompatible with the target.
- **Adapter**: A class that wraps the adaptee to provide the target interface.


## The Anatomy of the Adapter Pattern
- **Target Interface**: This defines the domain-specific interface that the client expects to interact with.
- **Adaptee**: The class that you want to adapt. Its interface is incompatible with the Target interface.
- **Adapter**: The class that `adapts` the Adaptee to the Target interface by converting the method calls.

## Real-World Example
Let’s consider a media player example. We have an existing `MP3 player`, but we also want to add the ability to play `MP4` and `VLC files`. Since the MP3 player doesn't have a method to play MP4 or VLC files, we can use the Adapter pattern.

- **Adaptee**: The existing MP3 player, which can only play MP3 files.
- **Target**: A universal MediaPlayer interface that can play MP3, MP4, and VLC files.
- **Adapter**: The adapter will wrap the MP4 and VLC players to make them compatible with the MediaPlayer interface.

## Detailed Explanation of the Adapter's Working
- **Adapter Initialization**: The `UniversalChargerAdapter` receives either a `USBCharger` or `MicroUSBCharger` or a `TypeCCharger` instance. It doesn't modify the original charger class but uses it in a way that conforms to the Charger interface.
- **Method Mapping**: The Adapter receives the request to charge a device and maps it to the appropriate method (charge_with_usb, charge_with_type_c or charge_with_micro_usb) depending on the type of the adapter.

## The Benefits of Using the Adapter Pattern
- **Separation of Concerns**: The Adapter pattern allows you to keep the client code and legacy code separate. The client interacts only with the Charger interface, never directly with the USBCharger or MicroUSBCharger.
- **Flexibility**: You can easily add more types of chargers or devices by creating new Adapters without modifying existing code.
- **Reusability**: The Adapter pattern promotes code reuse. For example, you could reuse the same adapter code with different devices and chargers.
- **Loose Coupling**: The Adapter pattern decouples the client from the implementation details of the Adaptee.


## Possible Drawbacks and Considerations
- **Overuse of Adapters**: If used excessively, the Adapter pattern can lead to a lot of classes, which may make the system harder to maintain.
- **Complexity**: Adapting multiple different systems through multiple layers of adapters can introduce unnecessary complexity.
- **Interface Mismatch**: If the Adaptee’s interface is too different from the Target’s expected behavior, the Adapter class can become very complicated.


## Real-World Use Cases
Here are some real-world examples of Adapter Pattern in software systems:

- **Database Connectivity**: When you need to work with databases that have different connection protocols or configurations, an adapter can help standardize the interaction.
- **UI Frameworks**: In GUI-based applications, you might need an adapter to work with various libraries like PyQt, tkinter, or Kivy, each having its own way of defining buttons or forms.
- **Third-Party Integration**: When integrating with external APIs or services, where the API doesn't follow the expected structure, the Adapter can convert responses into the format your system expects.

## Key Takeaways
- Inheritance is not required for Adaptee classes because they represent existing, incompatible implementations. Their purpose is to provide specific functionality, not conform to the Target Interface.
- The Adapter should conform to the Target Interface (often using inheritance or interface implementation).
- Composition is preferred over inheritance for adapting Adaptees, as it offers greater flexibility, decoupling, and reusability.
