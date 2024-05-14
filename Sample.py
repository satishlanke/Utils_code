import tkinter as tk

def button_clicked():
    print("Button clicked!")

# Create the main tkinter window
root = tk.Tk()
root.title("Text and Button App")

# Create a frame to hold the widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

# Create a label widget for displaying text on the left side
text_label = tk.Label(frame, text="Left Text", padx=10, pady=10)
text_label.pack(side=tk.LEFT)

# Create a button widget on the right side
button = tk.Button(frame, text="Click Me", command=button_clicked, width=10)
button.pack(side=tk.RIGHT)

# Start the main tkinter event loop
root.mainloop()
