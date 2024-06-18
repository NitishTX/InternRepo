import os
import sys
import shutil
from abc import ABC, abstractmethod

# Base class for all operations
class Operation(ABC):
    @abstractmethod
    def execute(self):
        pass

# File operation classes inheriting from Operation
class CreateFileOperation(Operation):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        with open(self.file_name, 'w') as f:
            f.write("")
        return f"File '{self.file_name}' created."

class DeleteFileOperation(Operation):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            return f"File '{self.file_name}' deleted."
        else:
            return f"File '{self.file_name}' not found."

class ReadFileOperation(Operation):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                return f.read()
        else:
            return f"File '{self.file_name}' not found."

class WriteToFileOperation(Operation):
    def __init__(self, file_name, content):
        self.file_name = file_name
        self.content = content

    def execute(self):
        with open(self.file_name, 'a') as f:
            f.write(self.content + "\n")
        return f"Content written to '{self.file_name}'."

class RenameFileOperation(Operation):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def execute(self):
        if os.path.exists(self.old_name):
            os.rename(self.old_name, self.new_name)
            return f"File '{self.old_name}' renamed to '{self.new_name}'."
        else:
            return f"File '{self.old_name}' not found."

class CopyFileOperation(Operation):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def execute(self):
        if os.path.exists(self.source):
            shutil.copy(self.source, self.destination)
            return f"File '{self.source}' copied to '{self.destination}'."
        else:
            return f"File '{self.source}' not found."

class CheckFileExistsOperation(Operation):
    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        if os.path.exists(self.file_name):
            return f"File '{self.file_name}' exists."
        else:
            return f"File '{self.file_name}' does not exist."

# User input handling
class UserInput:
    def get_user_input_file_operations(self):
        print("Select file operation:")
        print("1. Create File")
        print("2. Delete File")
        print("3. Read File")
        print("4. Write to File")
        print("5. Rename File")
        print("6. Copy File")
        print("7. Check if File Exists")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice")
            sys.exit()

        file_name = input("Enter the file name: ")

        if choice == '4':
            content = input("Enter the content to write: ")
            return choice, file_name, content
        elif choice == '5':
            new_name = input("Enter the new file name: ")
            return choice, file_name, new_name
        elif choice == '6':
            destination = input("Enter the destination file name: ")
            return choice, file_name, destination
        else:
            return choice, file_name

# Main application class
class Main:
    def __init__(self):
        self.user_input = UserInput()

    def main(self):
        choice, file_name, *extra_args = self.user_input.get_user_input_file_operations()

        operation = None

        if choice == '1':
            operation = CreateFileOperation(file_name)
        elif choice == '2':
            operation = DeleteFileOperation(file_name)
        elif choice == '3':
            operation = ReadFileOperation(file_name)
        elif choice == '4':
            operation = WriteToFileOperation(file_name, extra_args[0])
        elif choice == '5':
            operation = RenameFileOperation(file_name, extra_args[0])
        elif choice == '6':
            operation = CopyFileOperation(file_name, extra_args[0])
        elif choice == '7':
            operation = CheckFileExistsOperation(file_name)

        if operation:
            result = operation.execute()
            print(result)

        next_operation = input("Do you want to perform another operation? (yes/no): ")
        if next_operation.lower() == 'yes':
            self.main()

if __name__ == "__main__":
    main_app = Main()
    main_app.main()
