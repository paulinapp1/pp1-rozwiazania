# Open the original file in read mode
with open('data.txt', 'r', encoding="utf-8") as original_file:
    # Read lines from the original file
    lines = original_file.readlines()

    # Open or create the copylines.txt file in write mode
    with open('copylines.txt', 'w') as copy_file:
        # Write each line to the copylines.txt file
        for line in lines:
            copy_file.write(line)

print("Contents copied successfully.")
