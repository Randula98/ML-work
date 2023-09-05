import tkinter as tk

# Create a function to be called when the button is clicked


def on_button_click():
    label.config(text="Hello, " + entry.get())


# Create the main application window
app = tk.Tk()
app.title("Simple GUI Example")

# Create a label widget
label = tk.Label(app, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(app)
entry.pack()

# Create a button widget
button = tk.Button(app, text="Greet", command=on_button_click)
button.pack()

# Start the main event loop
app.mainloop()
