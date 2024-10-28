from temp import Thermometer
import random
temperature=Thermometer(random.uniform(34.0, 42.0))

temperature.turn_on()
temperature.check_temperature()