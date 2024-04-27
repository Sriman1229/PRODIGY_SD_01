import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"Temperature in Fahrenheit: {fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"Temperature in Celsius: {celsius:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Celsius to Fahrenheit conversion
celsius_frame = tk.Frame(root, bg="#f0f0f0")
celsius_frame.pack(pady=10)

celsius_label = tk.Label(celsius_frame, text="Enter temperature in Celsius:", font=("Arial", 12), bg="#f0f0f0")
celsius_label.grid(row=0, column=0, padx=(10, 5), pady=10)

celsius_entry = tk.Entry(celsius_frame, font=("Arial", 12), justify="center")
celsius_entry.grid(row=0, column=1, padx=5, pady=10)

c_to_f_button = tk.Button(celsius_frame, text="Convert to Fahrenheit", font=("Arial", 12), command=celsius_to_fahrenheit)
c_to_f_button.grid(row=0, column=2, padx=5, pady=10)

# Fahrenheit to Celsius conversion
fahrenheit_frame = tk.Frame(root, bg="#f0f0f0")
fahrenheit_frame.pack(pady=10)

fahrenheit_label = tk.Label(fahrenheit_frame, text="Enter temperature in Fahrenheit:", font=("Arial", 12), bg="#f0f0f0")
fahrenheit_label.grid(row=0, column=0, padx=(10, 5), pady=10)

fahrenheit_entry = tk.Entry(fahrenheit_frame, font=("Arial", 12), justify="center")
fahrenheit_entry.grid(row=0, column=1, padx=5, pady=10)

f_to_c_button = tk.Button(fahrenheit_frame, text="Convert to Celsius", font=("Arial", 12), command=fahrenheit_to_celsius)
f_to_c_button.grid(row=0, column=2, padx=5, pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
