import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="black")
    elif length < 6:
        result_label.config(text="Weak Password", fg="red")
    elif 6 <= length <= 10:
        result_label.config(text="Medium Strength Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Label
label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the app
root.mainloop()