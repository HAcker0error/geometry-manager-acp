import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    name = entry_name.get().strip()
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        if not name:
            messagebox.showerror("Input Error", "Please enter a name.")
            return
        birth_date = date(year, month, day)
        today = date.today()
        if birth_date > today:
            messagebox.showerror("Input Error", "Birth date cannot be in the future.")
            return
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        label_result.config(text=f"Hello {name}!\nYou are {age} years old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for date, month, and year.")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), pady=15)
title_label.pack()

grid_frame = tk.Frame(root, padx=20, pady=10)
grid_frame.pack()

tk.Label(grid_frame, text="Name:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=8, padx=5)
entry_name = tk.Entry(grid_frame, font=("Arial", 11), width=18)
entry_name.grid(row=0, column=1, pady=8, padx=5)

tk.Label(grid_frame, text="Birth Date (DD):", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8, padx=5)
entry_day = tk.Entry(grid_frame, font=("Arial", 11), width=18)
entry_day.grid(row=1, column=1, pady=8, padx=5)

tk.Label(grid_frame, text="Birth Month (MM):", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=8, padx=5)
entry_month = tk.Entry(grid_frame, font=("Arial", 11), width=18)
entry_month.grid(row=2, column=1, pady=8, padx=5)

tk.Label(grid_frame, text="Birth Year (YYYY):", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=8, padx=5)
entry_year = tk.Entry(grid_frame, font=("Arial", 11), width=18)
entry_year.grid(row=3, column=1, pady=8, padx=5)

btn_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
btn_calculate.pack(pady=20)

label_result = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="#1eed2c", justify="center")
label_result.pack(pady=10)

root.mainloop()