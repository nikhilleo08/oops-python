# Target Interface
class Charger:
    """Target Interface: This is the interface expected by the client."""
    def charge(self, device):
        raise NotImplementedError("This method should be overridden by the adapter")

class UsbCharger:
    """Adaptee: USB charger interface for USB devices."""
    def charge_with_usb(self, device):
        print(f'Charging the {device} with USB Charger')

class TypeCCharger:
    """Adaptee: Type-C charger interface for Type-C devices."""
    def charge_with_type_c(self, device):
        print(f'Charging the {device} with Type C Charger')


class MicroUSBCharger:
    """Adaptee: Micro-USB charger interface for micro-USB devices."""
    def charge_with_micro_usb(self, device):
        print(f"Charging {device} with Micro-USB port.")


class UniversalChargerAdapter(Charger):
    """Adapter: Adapts USBCharger, TypeCCharger and MicroUSBCharger to the Charger interface."""
    def __init__(self, charger):
        super().__init__()
        self.charger = charger
    
    def charge(self, device):
        if isinstance(self.charger, UsbCharger):
            self.charger.charge_with_usb(device)
            return
        elif isinstance(self.charger, MicroUSBCharger):
            self.charger.charge_with_micro_usb(device)
            return
        elif isinstance(self.charger, TypeCCharger):
            self.charger.charge_with_type_c(device)
            return
        else:
            raise ValueError(f"Unsupported charger type {type(self.charger)}")

usb_charger = UsbCharger()
micro_usb_charger = MicroUSBCharger()
type_c_charger = TypeCCharger()

generic_charger = UniversalChargerAdapter(usb_charger)
generic_charger.charge("Samsung Phone")

generic_charger = UniversalChargerAdapter(micro_usb_charger)
generic_charger.charge("OnePlus Phone")

generic_charger = UniversalChargerAdapter(type_c_charger)
generic_charger.charge("Nokia Phone")

generic_charger = UniversalChargerAdapter(TypeCCharger())
generic_charger.charge("Hello Phone")

