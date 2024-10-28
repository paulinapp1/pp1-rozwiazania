class Phones:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        self.turned_on=False
        self.locked=True
        self.connected_to_internet=False
    def status(self):
        return self.locked, self.turned_on, self.connected_to_internet
    def turn_on(self):
        self.turned_on=True
    def turn_off(self):
        self.turned_on=False
    def lock(self):
        self.locked=True
    def unlock(self):
        self.locked=False
    def connect(self):
        self.connected_to_internet=True
    def disconnect(self):
        self.connected_to_internet=False


phone1=Phones("Samsung","S21")
phone1.turn_on()
phone1.connect()
phone1.unlock()
print(phone1.status())

    
    
        