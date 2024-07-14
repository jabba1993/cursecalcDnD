import tkinter as tk
from tkinter import ttk

def calculate_total():
    try:
        # Retrieve values from entry widgets
        spellbook_value = float(entry_spellbook.get())
        power_value = float(entry_power.get())
        curseofpain_value = float(entry_curseofpain.get())
        add_value = float(entry_add.get())
        magicalresist_value = float(entry_magicalresist.get())
        penetration_value = float(entry_penetration.get())
        true_value = float(entry_true.get())
        
        # Constants
        location = 1
        projectilereduction = 1
        
        # Calculate magpowerbonus
        magpowerbonus = 1 + power_value
        
        # Calculate total
        total = ((((curseofpain_value + spellbook_value) * magpowerbonus + add_value) * location * 
                  (1 - magicalresist_value * (1 - penetration_value)) * projectilereduction) + true_value)
        
        # Update result label with calculated total
        result_label.config(text=f"Total = {total:.2f}")
        
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Create main window
root = tk.Tk()
root.title("Spellbook Calculator")

# Create labels and entry widgets for inputs
labels = ["Spellbook:", "Power:", "Curse of Pain:", "Add:", 
          "Magical Resist:", "Penetration:", "True:"]
entries = {}

for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.E)
    
    entry = ttk.Entry(root, width=10)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label_text] = entry

# Assigning specific entries to variables
entry_spellbook = entries["Spellbook:"]
entry_power = entries["Power:"]
entry_curseofpain = entries["Curse of Pain:"]
entry_add = entries["Add:"]
entry_magicalresist = entries["Magical Resist:"]
entry_penetration = entries["Penetration:"]
entry_true = entries["True:"]

# Create button to calculate
calculate_button = ttk.Button(root, text="Calculate", command=calculate_total)
calculate_button.grid(row=len(labels), columnspan=2, padx=10, pady=10)

# Create label to display result
result_label = ttk.Label(root, text="")
result_label.grid(row=len(labels) + 1, columnspan=2, padx=10, pady=5)

# Start the main loop
root.mainloop()
