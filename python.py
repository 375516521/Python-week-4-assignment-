# File Read & Write with Error Handling

try:
    # Ask the user for a file name
    filename = input("Enter the filename you want to read: ")

    # Open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (example: make it uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified file has been saved as {new_filename}")

# Handle errors if file does not exist
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")

# Handle errors if file can’t be read
except PermissionError:
    print("Error: You don’t have permission to read this file.")

# Handle any other error
except Exception as e:
    print("An unexpected error occurred:", e)
