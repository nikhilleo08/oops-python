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


