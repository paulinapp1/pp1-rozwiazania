class Phone():
    def __init__(self,owner, battery_level, phone_number):
        self.lockscreen=False
        self.new_phone=1
        self.owner=owner
        self.battery_level=battery_level
        self.phone_number=phone_number
    def check_battery_status(self, battery_level):
        self.battery_level=battery_level
    def is_lockscreen(self):
        self.lockscreen=True
    def change_phonenum(self,phone_number):
        self.new_phone=phone_number

phone=Phone("Paulina", "49", "123123123")
print(f"The owner of the phone is{phone.owner}", end="")
print(f"the current battery level is {phone.battery_level}", end="")
print(f"The phone number is {phone.phone_number}", end="")
phone.is_lockscreen()
if phone.is_lockscreen:
    print("This phone has a lockscreen")
phone.change_phonenum("333222111")
print(f"The new phone number is: {phone.new_phone}")





    
        
