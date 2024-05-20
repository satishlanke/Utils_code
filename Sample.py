import tkinter as tk
from tkinter import ttk

def create_progress_bars():
    for i in range(5):  # Create 5 progress bars as an example
        progress = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="determinate")
        progress.grid(row=i, column=1, pady=5)
        progress['value'] = (i + 1) * 20  # Example progress value

# Initialize main window
root = tk.Tk()
root.title("Tkinter Interface Example")

# Configure grid layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# Main frame
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Left side label
project_label = tk.Label(main_frame, text="Project Name", font=("Arial", 16))
project_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

# Right side button
generate_button = tk.Button(main_frame, text="Generate Progress Bars", command=create_progress_bars)
generate_button.grid(row=0, column=1, padx=20, pady=20, sticky="e")

# Run the application
root.mainloop()
