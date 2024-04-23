import tkinter as tk
from tkinter import messagebox
import hashlib


def login():
    username = entry_username.get()
    password = entry_password.get()

    
    with open("users.txt", "r") as f:
        users_data = f.readlines()

    for user_data in users_data:
        stored_username, stored_password = user_data.strip().split(":")
        if username == stored_username:
            
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == stored_password:
                messagebox.showinfo("Login Berhasil", "Selamat Datang, " + username + "!")
                return

    messagebox.showerror("Login Gagal", "Username atau password invalid")


def show_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Registrasi")

    
    label_username = tk.Label(register_window, text="Username:")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(register_window)
    entry_username.grid(row=0, column=1)

    label_password = tk.Label(register_window, text="Password:")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(register_window, show="*")
    entry_password.grid(row=1, column=1)

    
    register_button = tk.Button(register_window, text="Register", command=lambda: register(entry_username.get(), entry_password.get()))
    register_button.grid(row=2, column=0, columnspan=2, pady=5)


def register(username, password):
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    
    with open("users.txt", "a") as f:
        f.write(username + ":" + hashed_password + "\n")

    messagebox.showinfo("Registrasi Berhasil", "Akun berhasil dibuat")


with open("users.txt", "a") as f:
    pass


root = tk.Tk()
root.title("Login")


label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)


label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)


login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=5)


register_button = tk.Button(root, text="Register", command=show_register_window)
register_button.grid(row=3, column=0, columnspan=2, pady=5)


root.mainloop()
