# Level 1: Grandparent Class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is now ON.")

# Level 2: Parent Class (Inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model):
        # Grandparent ka constructor call karna
        super().__init__(brand)
        self.model = model

    def connect_internet(self):
        print(f"{self.model} is connecting to 5G...")

# Level 3: Child Class (Inherits from Smartphone)
class AndroidPhone