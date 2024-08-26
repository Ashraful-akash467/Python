import tkinter as tk

def say_hello():
    print("Hello, World!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a button widget
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

# Start the main event loop
root.mainloop()
