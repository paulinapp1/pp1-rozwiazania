def month(n):
    # Array of month names
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    
    # Check if the month number is within a valid range
    if 1 <= n <= 12:
        return month_names[n - 1]  # Adjust index since month numbers start from 1
    else:
        return "Invalid month number"

# Display month names for the specified month numbers
months_to_display = [1, 2, 11, 12]

for month_number in months_to_display:
    month_name = month(month_number)
    print(f"Month {month_number}: {month_name}")