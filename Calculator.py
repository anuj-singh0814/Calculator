import customtkinter as ctk

# Set appearance mode and theme
ctk.set_appearance_mode("dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Define button callback functions
def button_click(number):
    current = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, ctk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, ctk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, ctk.END)
        entry.insert(0, "Error")

# Create the main window
root = ctk.CTk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Entry widget
entry = ctk.CTkEntry(root, width=300, height=50, font=("Helvetica", 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add rounded buttons
for (text, row, col) in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    else:
        cmd = lambda t=text: button_click(t)

    btn = ctk.CTkButton(root, text=text, width=60, height=60, corner_radius=30, font=("Helvetica", 18), command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
