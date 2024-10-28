def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                content = source.read()  # Read the entire content of the source file
                destination.write(content)  # Write the content to the destination file
        print(f"File '{source_file}' has been copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please provide valid file names.")

# Replace 'source_file.txt' and 'copy.txt' with your file names
source_file = 'source_file.txt'
destination_file = 'copy.txt'

copy_file(source_file, destination_file)
