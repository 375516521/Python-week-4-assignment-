# File Read & Write with Error Handling

This Python program demonstrates how to **read from a file, modify its content, and write the modified version to a new file** while handling common errors gracefully.

## Features
- Prompts the user to enter the filename they want to read.
- Reads the file content.
- Transforms the content (in this case, converts text to uppercase).
- Saves the modified content into a new file prefixed with `modified_`.
- Handles common errors such as:
  - **FileNotFoundError** → when the file doesn’t exist.
  - **PermissionError** → when the file cannot be accessed.
  - **Other Exceptions** → any other unexpected issues.

## How It Works
1. The user is asked to input the filename.
2. The program opens the file in read mode (`r`).
3. The file content is read and modified (to uppercase).
4. A new file is created with the prefix `modified_` followed by the original filename.
5. The modified content is saved into this new file.

**Example:**
If you enter `example.txt`, the program will create a new file named `modified_example.txt`.

## Example Run

bash
Enter the filename you want to read: example.txt
Modified file has been saved as modified_example.txt

