import re

# The text containing temperature forecasts
forecast_text = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

# Find all temperature values using regex
temperatures = re.findall("\d{2}", forecast_text)

# Extracted temperatures as integers
temperature_values = [int(temp[:-1]) for temp in temperatures]  # Removing 'C' and converting to integers

# Calculate average temperature
if temperature_values:
    average_temperature = sum(temperature_values) / len(temperature_values)
    print(f"The average temperature for the next three days is: {average_temperature:.2f}°C")
else:
    print("No temperature data found.")
