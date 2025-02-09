from abc import ABC, abstractmethod

# Step 1: Define Abstract Product Interfaces
class Button(ABC):
    """Abstract Product: Button"""
    @abstractmethod
    def render(self):
        pass

class CheckBox(ABC):
    """Abstract Product: CheckBox"""
    @abstractmethod
    def render(self):
        pass

# Step 2: Define Concrete Product Classes (Windows Variants)
class WindowsButton(Button):
    """Concrete Product: Windows Button"""
    def render(self):
        print("Rendering Windows Styled Button")

class WindowsCheckBox(CheckBox):
    """Concrete Product: Windows Checkbox"""
    def render(self):
        print("Rendering Windows Styled CheckBox")

# Step 3: Create Concrete Product Classes (Mac Variants)
class MacButton(Button):
    """Concrete Product: Mac Button"""
    def render(self):
        print("Rendering Mac Styled Button")

class MacCheckBox(CheckBox):
    """Concrete Product: Mac Checkbox"""
    def render(self):
        print("Rendering Mac Styled CheckBox")

# Step 4: Define the Abstract Factory Interface
class GUIFactory(ABC):
    """Abstract Factory: GUIFactory"""
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Step 5: Implement Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckBox()
    
class MacFactory(GUIFactory):
    """Concrete Factory: Mac UI Factory"""
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> CheckBox:
        return MacCheckBox()

# Global Factory Registry
_factory_registry = {
    "windows": WindowsFactory,
    "mac": MacFactory
}

# Step 6: Function to Register a New Factory
def register_factory(os_type: str, factory_class: GUIFactory):
    """Dynamically register a new OS factory"""
    if not issubclass(factory_class, GUIFactory):
        raise ValueError(f"{factory_class} must be a subclass of GUIFactory")
    _factory_registry[os_type] = factory_class

# Step 7: Factory Retrieval Function
def get_factory(os_type='windows'):
    # Default factory is windows factory
    if os_type not in _factory_registry:
        print(f"Wrong OS type input {os_type}, defaulting to Windows Themed Components")
        return WindowsFactory()
    return _factory_registry[os_type]()


factory = get_factory('mac')
factory.create_button().render()
factory.create_checkbox().render()

factory = get_factory('windows')
factory.create_button().render()
factory.create_checkbox().render()

factory = get_factory('abac')
factory.create_button().render()
factory.create_checkbox().render()

# Step 8: Create Concrete Product Classes (Linux Variants)
class LinuxButton(Button):
    def render(self):
        print("Rendering Linux Styled Button")

class LinuxCheckBox(CheckBox):
    def render(self):
        print("Rendering Linux Styled CheckBox")

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_checkbox(self):
        return LinuxCheckBox()

# Register Linux Factory Dynamically
register_factory("linux", LinuxFactory)

# Test Newly Registered Factory
factory = get_factory('linux')
factory.create_button().render()
factory.create_checkbox().render()
