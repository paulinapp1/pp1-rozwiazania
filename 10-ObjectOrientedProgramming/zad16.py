class Phones():
    def __init__(self, color, battery,pin_code ):
        self.color=color
        self.battery=battery
        self.pin_code=pin_code
    def battery_level(self):
        if self.battery<=5:
            print("Charge your phone")
        else:
            print("You don't need to charge your phone")
    def pin(self, enter):
        if self.pin_code==enter:
            print("Pin is correst")
        else:
            print("Pin is incorrect")

my_phone=Phones("black", 40, 3333)
my_phone.battery_level()
my_phone.pin(1234)
        
