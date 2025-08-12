import tkinter as tk
from tkinter import ttk

# Function to update expression
def press(key):
    current = entry_var.get()
    if key == "C":
        entry_var.set("")
    elif key == "=":
        try:
            result = str(eval(current))
            entry_var.set(result)
            history_list.insert(tk.END, current + " = " + result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(current + key)

def clear_history():
    history_list.delete(0, tk.END)

# Hover effects
def on_enter(e):
    e.widget.configure(background="#ffb6c1", foreground="black")  # pink hover
def on_leave(e, bg1, fg1):
    e.widget.configure(background=bg1, foreground=fg1)
def on_click(e):
    e.widget.configure(background="#FFD700", foreground="white")  # gold click

root = tk.Tk()
root.title("Tkinter Calculator - Styled")
root.geometry("600x500")
root.minsize(400, 400)
root.configure(bg="#e6e9f0")

# ---- Heading ----
heading = tk.Label(
    root, text="Simple Calculator",
    font=("Arial", 24, "bold"),
    fg="#ff4d4d", bg="#e6e9f0"
)
heading.pack(pady=10)

# ---- Left frame for history ----
left_frame = tk.Frame(root, width=180, bg="#f0f0f0")
left_frame.pack(side=tk.LEFT, fill=tk.Y)

history_label = tk.Label(left_frame, text="History", bg="#f0f0f0", font=("Arial", 12, "bold"))
history_label.pack(pady=5)

history_list = tk.Listbox(left_frame)
history_list.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

clear_history_btn = tk.Button(left_frame, text="Clear History", font=("Arial", 12, "bold"),
                               bg="#f5f5f5", fg="black", command=clear_history, relief="flat")
clear_history_btn.pack(pady=5, fill=tk.X)
clear_history_btn.bind("<Enter>", on_enter)
clear_history_btn.bind("<Leave>", lambda e: on_leave(e, "#f5f5f5", "black"))
clear_history_btn.bind("<ButtonPress-1>", on_click)
clear_history_btn.bind("<ButtonRelease-1>", lambda e: on_leave(e, "#f5f5f5", "black"))

# ---- Right frame for calculator ----
right_frame = tk.Frame(root, bg="#e0e0e0")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

entry_var = tk.StringVar()
entry = tk.Entry(right_frame, textvariable=entry_var, font=("Arial", 24),
                 bd=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10, sticky="nsew")

# Button style
btn_bg = "#edb167"
btn_fg = "black"

# Updated button layout with ( and )
buttons = [
    ("(", 1, 0), (")", 1, 1), ("C", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1)
]

# Create buttons
for (text, row, col) in buttons:
    b = tk.Button(right_frame, text=text, font=("Arial", 18), bg=btn_bg, fg=btn_fg,
                  command=lambda t=text: press(t), relief="flat")
    b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", lambda e, bg=btn_bg, fg=btn_fg: on_leave(e, bg, fg))
    b.bind("<ButtonPress-1>", on_click)
    b.bind("<ButtonRelease-1>", lambda e, bg=btn_bg, fg=btn_fg: on_leave(e, bg, fg))

# Equals button (full width)
eq_btn = tk.Button(right_frame, text="=", font=("Arial", 18), bg="#c1ffc1",
                   command=lambda: press("="), relief="flat")
eq_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
eq_btn.bind("<Enter>", on_enter)
eq_btn.bind("<Leave>", lambda e: on_leave(e, "#c1ffc1", "black"))
eq_btn.bind("<ButtonPress-1>", on_click)
eq_btn.bind("<ButtonRelease-1>", lambda e: on_leave(e, "#c1ffc1", "black"))

# Responsive resizing
for i in range(4):
    right_frame.columnconfigure(i, weight=1)
for i in range(6):
    right_frame.rowconfigure(i, weight=1)

root.mainloop()
