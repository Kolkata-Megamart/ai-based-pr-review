import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(expression)
            entry_value.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            entry_value.set("")
    elif text == "C":
        expression = ""
        entry_value.set("")
    else:
        expression += text
        entry_value.set(expression)

# Initialize application
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
expression = ""

entry_value = tk.StringVar()
entry = tk.Entry(root, textvar=entry_value, font=('Arial', 18), justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

# Creating buttons and assigning to grid 
row, col = 0, 0
for button_text in buttons:
    btn = tk.Button(button_frame, text=button_text, font=('Arial', 16), padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
root.mainloop()
