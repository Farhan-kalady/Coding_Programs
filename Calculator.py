import tkinter as tk

# Function to update the screen when buttons are clicked
def press_button(char):
    if char == 'C':
        screen_var.set("") # Clear screen
    elif char == '=':
        try:
            # Safely evaluate the mathematical expression on screen
            result = str(eval(screen_var.get()))
            screen_var.set(result)
        except Exception:
            screen_var.set("Error")
    else:
        screen_var.set(screen_var.get() + str(char))

# Setup the main application window
root = tk.Tk()
root.title("Easy Calculator")

# Variable to track screen text
screen_var = tk.StringVar()

# Create the display screen
screen = tk.Entry(root, textvariable=screen_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=5, justify='right')
screen.grid(row=0, column=0, columnspan=4)

# Define calculator buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Generate buttons automatically using a loop
row_idx = 1
col_idx = 0
for btn_text in buttons:
    action = lambda x=btn_text: press_button(x)
    tk.Button(root, text=btn_text, padx=20, pady=20, font=("Arial", 14), command=action).grid(row=row_idx, column=col_idx)
    col_idx += 1
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

# Run the app window loop
root.mainloop()
