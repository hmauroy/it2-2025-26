import tkinter as tk

root = tk.Tk()
root.title("Toggle Button Row")

# Create a row of buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, pady=10)

buttons = []
for i in range(5):
    btn = tk.Button(button_frame, text=f"Button {i+1}")
    btn.grid(row=0, column=i, padx=5)
    buttons.append(btn)

# Track visibility state
visible = True

def toggle_buttons():
    global visible
    if visible:
        button_frame.grid_remove()  # Hide the entire frame
    else:
        button_frame.grid()  # Show it again
    visible = not visible

# Toggle button
toggle_btn = tk.Button(root, text="Toggle Buttons", command=toggle_buttons)
toggle_btn.grid(row=0, column=0, pady=10)

root.mainloop()