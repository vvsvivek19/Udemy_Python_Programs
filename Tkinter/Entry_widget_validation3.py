from tkinter import *

def validate_password():
    """
    Validate that the password meets certain criteria.
    Updates the label with a validation message.
    """
    password = entry.get()
    if len(password) < 8:
        validation_label.config(text="Password must be at least 8 characters long", fg="red")
    elif not any(char.isdigit() for char in password):
        validation_label.config(text="Password must contain at least one number", fg="red")
    elif not any(char.isupper() for char in password):
        validation_label.config(text="Password must contain at least one uppercase letter", fg="red")
    else:
        validation_label.config(text="Valid password", fg="green")

# Create the main window
root = Tk()
root.title("Password Validation Example")

# Create an Entry widget
entry = Entry(root, show='*')  # Use 'show' to hide the password
entry.pack(padx=10, pady=10)

# Create a button to trigger validation
validate_button = Button(root, text="Validate Password", command=validate_password)
validate_button.pack(padx=10, pady=5)

# Create a label to display the validation message
validation_label = Label(root, text="")
validation_label.pack(padx=10, pady=5)

# Run the main event loop
root.mainloop()
