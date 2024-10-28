file_name = input("Enter the name of the file: ")  
with open(file_name, "r") as file:
        lines = file.readlines()  # Read all lines into the 'lines' variable
        count = len(lines) 

print(f"{file_name}")
print(f"Number of lines {count}")

