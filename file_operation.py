import os
class FileOperation:
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        """Creates a new file if it does not already exist."""
        try:
            if not os.path.exists(self.file_name):
                with open(self.file_name, 'x'):
                    print(f"The file '{self.file_name}' has been created.")
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")

    def write_file(self) -> None:
        """Appends user input to the file until 'stop' is entered."""
        if not self.file_name:
            print("No file selected. Please create or specify a file first.")
            return
        print('Type "stop" to finish writing.')
        with open(self.file_name, 'a') as file:
            line_number = 1
            while True:
                line = input(f"Enter text for line {line_number}: ")
                if line.lower() == "stop":
                    print("Writing to the file has stopped.")
                    break
                file.write(line + '\n')
                line_number += 1

    def read_file(self) -> None:
        """Reads and displays the contents of the file."""
        if not self.file_name:
            print("No file selected. Please create or specify a file first.")
            return
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
                if content:
                    print(content)
                else:
                    print("The file is empty.")
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")

    def clear_file_content(self) -> None:
        """Clears the contents of the file."""
        if not self.file_name:
            print("No file selected. Please create or specify a file first.")
            return
        try:
            with open(self.file_name, 'r') as file:
                if file.read():
                    with open(self.file_name, 'w'):
                        print("The file contents have been cleared.")
                else:
                    print("The file is already empty.")
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")

    def update_file_content(self) -> None:
        """Updates a specific line in the file based on the user-provided line number."""
        if not self.file_name:
            print("No file selected. Please create or specify a file first.")
            return
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()

            if not lines:
                print("The file is empty. Nothing to update.")
                return

            print("Current file content:")
            for i, line in enumerate(lines, start=1):
                print(f"{i}: {line.strip()}")

            while True:
                try:
                    line_number = int(input("Enter the line number you want to update: "))
                    if 1 <= line_number <= len(lines):
                        break
                    else:
                        print(f"Invalid line number. Enter a number between 1 and {len(lines)}.")
                except ValueError:
                    print("Please enter a valid number.")

            new_content = input(f"Enter the new content for line {line_number}: ")
            lines[line_number - 1] = new_content + '\n'

            with open(self.file_name, 'w') as file:
                file.writelines(lines)

            print(f"Line {line_number} has been updated.")
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")

    def delete_file(self) -> None:
        """Deletes the file and its content permanently."""
        if not self.file_name:
            print("No file selected. Please create or specify a file first.")
            return
        try:
            os.remove(self.file_name)
            print(f"The file '{self.file_name}' has been deleted.")
            self.file_name = None
        except FileNotFoundError:
            print(f"The file '{self.file_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")

# Example usage:
file_ops: FileOperation = FileOperation("f1.txt")
# file_ops.write_file()
# file_ops.read_file()
# file_ops.update_file_content()
# file_ops.clear_file_content()
# file_ops.delete_file()

