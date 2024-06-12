import tkinter as tk
from tkinter import ttk, messagebox
import os
import pandas as pd
from threading import Thread

def list_excel_files():
    base_folder = '.'  # Change to your base folder if different
    files = [f for f in os.listdir(base_folder) if f.endswith('.xlsx') or f.endswith('.xls')]
    return files

def on_proceed():
    proceed_button.config(state="disabled")  # Disable the Proceed button
    files = list_excel_files()
    for file in files:
        file_label = ttk.Label(file_frame, text=file)
        file_label.grid(row=files.index(file), column=0, sticky="w")

def merge_excel_files():
    files = list_excel_files()
    if not files:
        return

    # Create and reset progress bars
    progress_bars = []
    for index, file in enumerate(files):
        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(file_frame, variable=progress_var, maximum=100)
        progress_bars.append((progress_bar, progress_var))
        progress_bar.grid(row=index, column=1, sticky="ew", padx=(0, 10))

    # Read and merge all Excel files
    merged_df = pd.DataFrame()
    for index, file in enumerate(files):
        df = pd.read_excel(file)
        merged_df = pd.concat([merged_df, df], ignore_index=True)
        progress_bars[index][1].set(100)  # Update the progress bar for the current file

    # Save the merged dataframe to a new Excel file
    merged_df.to_excel('merged_file.xlsx', index=False)
    
    # Inform the user that merging is complete
    # merge_label = ttk.Label(file_frame, text="Merging complete. Saved as 'merged_file.xlsx'.")
    # merge_label.grid(row=len(files), columnspan=2, sticky="w")
    messagebox.showinfo("Info", "Mearging the files completed successfully...")


def on_merge_button_click():
    merge_thread = Thread(target=merge_excel_files)
    merge_thread.start()

# Create the main window
root = tk.Tk()
root.title("German Tax Automation")

# Set the geometry of the window
root.geometry("400x400")

# Create a frame to hold the title and buttons
top_frame = ttk.Frame(root, padding="10")
top_frame.pack(side=tk.TOP, fill=tk.X)

# Create the title label
title_label = ttk.Label(top_frame, text="German Tax Automation", font=("Helvetica", 16))
title_label.pack(side=tk.LEFT, anchor='w')

# Create the proceed button
proceed_button = ttk.Button(top_frame, text="Proceed", command=on_proceed)
proceed_button.pack(side=tk.RIGHT, anchor='e')

# Create the merge button
merge_button = ttk.Button(top_frame, text="Merge", command=on_merge_button_click)
merge_button.pack(side=tk.RIGHT, anchor='e', padx=5)

# Create a frame to hold the file list and progress bars
file_frame = ttk.Frame(root, padding="10")
file_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()





import tkinter as tk
from tkinter import ttk, messagebox
import os
import pandas as pd
from threading import Thread

class GermanTaxAutomationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("German Tax Automation")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the title and buttons
        self.top_frame = ttk.Frame(self, padding="10")
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the title label
        self.title_label = ttk.Label(self.top_frame, text="German Tax Automation", font=("Helvetica", 16))
        self.title_label.pack(side=tk.LEFT, anchor='w')

        # Create the proceed button
        self.proceed_button = ttk.Button(self.top_frame, text="Proceed", command=self.on_proceed)
        self.proceed_button.pack(side=tk.RIGHT, anchor='e')

        # Create the merge button
        self.merge_button = ttk.Button(self.top_frame, text="Merge", command=self.on_merge_button_click)
        self.merge_button.pack(side=tk.RIGHT, anchor='e', padx=5)

        # Create a frame to hold the file list and progress bars
        self.file_frame = ttk.Frame(self, padding="10")
        self.file_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def list_excel_files(self):
        base_folder = '.'  # Change to your base folder if different
        files = [f for f in os.listdir(base_folder) if f.endswith('.xlsx') or f.endswith('.xls')]
        return files

    def on_proceed(self):
        self.proceed_button.config(state="disabled")  # Disable the Proceed button
        files = self.list_excel_files()
        for file in files:
            file_label = ttk.Label(self.file_frame, text=file)
            file_label.grid(row=files.index(file), column=0, sticky="w")

    def merge_excel_files(self):
        files = self.list_excel_files()
        if not files:
            return

        # Create and reset progress bars
        progress_bars = []
        for index, file in enumerate(files):
            progress_var = tk.DoubleVar()
            progress_bar = ttk.Progressbar(self.file_frame, variable=progress_var, maximum=100)
            progress_bars.append((progress_bar, progress_var))
            progress_bar.grid(row=index, column=1, sticky="ew", padx=(0, 10))

        # Read and merge all Excel files
        merged_df = pd.DataFrame()
        for index, file in enumerate(files):
            df = pd.read_excel(file)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
            progress_bars[index][1].set(100)  # Update the progress bar for the current file

        # Save the merged dataframe to a new Excel file
        merged_df.to_excel('merged_file.xlsx', index=False)
        
        # Inform the user that merging is complete
        messagebox.showinfo("Info", "Merging the files completed successfully...")

    def on_merge_button_click(self):
        merge_thread = Thread(target=self.merge_excel_files)
        merge_thread.start()

if __name__ == "__main__":
    app = GermanTaxAutomationApp()
    app.mainloop()


First, I would like to clarify that I have only participated in one call, not several, and I still have some unresolved queries. In our discussions, it appears there is some confusion regarding the two different approaches outlined in the Word document.From my understanding, Option Two is the IT solution intended for development, as highlighted in our previous call. Option One, on the other hand, seems to present the current process for Inka and DWS with minor enhancements. However, it remains unclear to me which solution is considered the most user-friendly and straightforward, as both options seem to overlap in their objectives.To move forward effectively, I kindly request a clear outline of what is expected from our side. Specifically, I would appreciate it if you could:Confirm which solution (Option One or Option Two) is being prioritized for development.Provide a detailed description of the final expected outcome.Clarify any additional inputs or actions required from our team.Your prompt response will help us align our efforts and ensure that we are on the same page moving forward.
