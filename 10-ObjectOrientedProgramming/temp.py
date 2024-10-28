class Thermometer:
    def __init__(self, temp):
        self.temp = temp
        self.is_on = False

    def check_temperature(self):
        if self.is_on:
            if self.temp < 37.0:
                print(f"Temperature: {self.temp}")
            elif 37.0 <= self.temp < 41.0:
                print(f"Temperature: {self.temp} (fever)")
            else:
                print(f"Temperature: {self.temp} CRITICAL TEMPERATURE!!")
        else:
            print("Turn on the thermometer to check temperature.")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

