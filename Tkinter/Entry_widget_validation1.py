from tkinter import *

def validate_numeric_input(new_value):
    """
    Validate that the input is a positive integer.
    Returns True if valid, False otherwise.
    """
    # Allow empty input (optional)
    if new_value == "":
        return True

    # Check if the input is a valid positive integer
    return new_value.isdigit()

# Create the main window
root = Tk()
root.title("Entry Validation Example")

# Register the validation function
validate_cmd = root.register(validate_numeric_input)

# Create an Entry widget with validation
entry = Entry(
    root, 
    validate="key", 
    validatecommand=(validate_cmd, "%P")  # %P passes the new value of the Entry
)
entry.pack(padx=10, pady=10)

# Create a label to display the entered text
label = Label(root, text="Enter a number:")
label.pack(padx=10, pady=5)

# Run the main event loop
root.mainloop()
