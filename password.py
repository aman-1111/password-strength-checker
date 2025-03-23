import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    score = 5 - sum(errors)

    if score == 5:
        result = "✅ Strong Password 💪"
        color = "green"
    elif score >= 3:
        result = "⚠️ Medium Strength"
        color = "orange"
    else:
        result = "❌ Weak Password"
        color = "red"

    result_label.config(text=result, fg=color)

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text='Hide Password')
    else:
        entry.config(show='*')
        toggle_button.config(text='Show Password')

# **🚀 GUI Setup**
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")  # 👈 Bigger Window
root.configure(bg="#EAF6F6")

# **Heading**
title_label = tk.Label(root, text="🔐 Enter Your Password", font=("Arial", 18, "bold"), bg="#EAF6F6")
title_label.pack(pady=20)

# **Password Entry Box**
entry = tk.Entry(root, show="*", font=("Arial", 16), width=30)
entry.pack(pady=10)

# **Toggle Password Button**
toggle_button = tk.Button(root, text="Show Password", command=toggle_password, 
                          font=("Arial", 14, "bold"), bg="#008CBA", fg="white", padx=10, pady=5)
toggle_button.pack(pady=5)

# **Check Strength Button**
check_button = tk.Button(root, text="Check Strength", command=check_password_strength, 
                         font=("Arial", 14, "bold"), bg="#008CBA", fg="white", padx=10, pady=5)
check_button.pack(pady=15)

# **Result Label**
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#EAF6F6")
result_label.pack(pady=10)

# **Run the GUI**
root.mainloop()
