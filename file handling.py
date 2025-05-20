def read_and_modify_file(filename):
    try:
        # Open the original file for reading
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Ask user for filename
user_filename = input("Enter the filename to read and modify: ")
read_and_modify_file(user_filename)
