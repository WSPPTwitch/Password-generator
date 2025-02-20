import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_special=True, use_letters=True, use_numbers=True):

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters")
        return ""
    
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        messagebox.showerror("Error", "You must select at least one character type")
        return ""
    
    password = ''.join(random.choices(char_pool, k=length))
    return password

def generate_and_display():
    try:
        length = int(length_entry.get())
        use_special = special_var.get()
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        
        password = generate_password(length, use_special, use_letters, use_numbers)
        if password:
            result_label.config(text=f"Generated password: {password}")
            copy_button.config(state=tk.NORMAL)
            root.clipboard_clear()
            root.clipboard_append(password)
            root.update()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")

def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated password: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Success", "Password copied")

# GUI Setup
root = tk.Tk()
root.title("Password generator")
root.geometry("300x300")

# Widgets
tk.Label(root, text="Password length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

special_var = tk.BooleanVar(value=True)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Special characters", variable=special_var).pack()
tk.Checkbutton(root, text="Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Numbers", variable=numbers_var).pack()

generate_button = tk.Button(root, text="Generate password", command=generate_and_display)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

root.mainloop()
