import tkinter as tk

class DualKeyApp:
    def __init__(self, root):
        self.root = root
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.bind('<KeyRelease>', self.on_key_release)
        self.keys_pressed = {} # Dictionary to store currently pressed keys
        
        self.label = tk.Label(root, text="Press W and Up Arrow together...")
        self.label.pack(pady=20)
        
        # Start the periodic check
        self.check_keys_periodically()

    def on_key_press(self, event):
        # Store the keysym (or char) as pressed
        self.keys_pressed[event.keysym] = True

    def on_key_release(self, event):
        # Mark the key as released
        if event.keysym in self.keys_pressed:
            del self.keys_pressed[event.keysym] # Remove to keep the dictionary clean

    def check_keys_periodically(self):
        print("check key...")
        # Check for the specific combination
        if 'w' in self.keys_pressed and 'Up' in self.keys_pressed:
            self.label.config(text="BOTH W and Up pressed simultaneously!")
        else:
            self.label.config(text="Press W and Up Arrow together...")
            
        # Reschedule the check (e.g., every 50 milliseconds)
        self.root.after(50, self.check_keys_periodically)

if __name__ == "__main__":
    root = tk.Tk()
    root.lift()
    root.title("DualKey")
    root.focus_force()
    app = DualKeyApp(root)
    root.mainloop()
