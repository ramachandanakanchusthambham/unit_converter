import tkinter as tk
from tkinter import ttk

# Conversion factors relative to meter
length_units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

def convert():
    try:
        input_value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        # Convert input to meters, then to desired unit
        value_in_meters = input_value * length_units[from_unit]
        result = value_in_meters / length_units[to_unit]
        
        label_result.config(text=f"{result:.4f} {to_unit}")
    except ValueError:
        label_result.config(text="Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")
root.resizable(False, False)

# Input field
tk.Label(root, text="Enter value:").pack(pady=5)
entry_value = tk.Entry(root, width=20)
entry_value.pack()

# From unit
tk.Label(root, text="From unit:").pack(pady=5)
combo_from = ttk.Combobox(root, values=list(length_units.keys()), state="readonly")
combo_from.current(0)
combo_from.pack()

# To unit
tk.Label(root, text="To unit:").pack(pady=5)
combo_to = ttk.Combobox(root, values=list(length_units.keys()), state="readonly")
combo_to.current(1)
combo_to.pack()

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Run the GUI
root.mainloop()
