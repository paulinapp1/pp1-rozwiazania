correct_pin = "0805"
attempts = 3

while attempts > 0:
    code = input("Enter your PIN code: ")
    if code == correct_pin:
            print("Correct PIN! Access granted.")
            break
    else:
        attempts=attempts-1
        if attempts > 0:
          print(f"Incorrect PIN! You have {attempts} attempt(s) left.")
        else:
                print("Incorrect PIN! Card blocked.")
                break