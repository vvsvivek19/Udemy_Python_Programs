from tkinter import *
import re

def validate_email(event):
    """
    Validate the email format.
    Updates the label with a validation message.
    """
    email = entry.get()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        validation_label.config(text="Valid email", fg="green")
    else:
        validation_label.config(text="Invalid email", fg="red")

# Create the main window
root = Tk()
root.title("Email Validation Example")

# Create an Entry widget
entry = Entry(root)
entry.pack(padx=10, pady=10)

# Bind the focusout event to the validation function
entry.bind("<FocusOut>", validate_email)

# Create a label to display the validation message
validation_label = Label(root, text="")
validation_label.pack(padx=10, pady=5)

# Run the main event loop
root.mainloop()
