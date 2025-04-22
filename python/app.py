import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password are correct (you can modify these)
    if username == "user" and password == "pass":
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Set window size
root.geometry("300x200")

# Username Label and Entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")  # hide password input
entry_password.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=10)

# Run the application
root.mainloop()
