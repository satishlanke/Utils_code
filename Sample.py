import os
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, filedialog
from tkinter import ttk

class FilePicker:
    def __init__(self):
        self.FileBrowsCount = 3
        self.file_labels = ["Loan Position Detail", "OEIC Earnings Repo Income", "OEICS Non Cash Collateral"]
        self.dropdown_values = ["Option 1", "Option 2", "Option 3"]
        
        self.UF = Tk()
        self.UF.title("File Picker")
        self.UF.geometry("700x400")
        
        # Entry frame setup
        Entry_frame = Frame(self.UF)
        Entry_frame.pack(side='top', fill='x')
        
        # Dictionary to store file paths
        self.fileListDict = {}
        
        # Labels, entry boxes, and browse buttons
        self.ref = []
        for i, label_text in enumerate(self.file_labels):
            lblFile = Label(Entry_frame, text=label_text)
            lblFile.grid(row=i, column=0, sticky='W', padx=10)
            
            txtFile = Entry(Entry_frame, state='disabled', width=50)
            txtFile.grid(row=i, column=1, padx=10, pady=5)
            self.ref.append(txtFile)
            
            btnBrowse = Button(Entry_frame, text="Browse", command=lambda idx=i: self.BrowseFile(idx))
            btnBrowse.grid(row=i, column=2, padx=5)
        
        # Dropdown for additional selection
        self.dropdown = ttk.Combobox(Entry_frame, values=self.dropdown_values)
        self.dropdown.set("Select an option")
        self.dropdown.grid(row=len(self.file_labels), column=1, padx=10, pady=10)
        
        # Submit Button
        btnSubmit = Button(Entry_frame, text="Submit", command=self.SubmitBtn)
        btnSubmit.grid(row=len(self.file_labels) + 1, column=1, sticky='W', padx=5, pady=10)

    def BrowseFile(self, indx):
        filename = filedialog.askopenfilename(initialdir=os.environ['USERPROFILE'] + "/Downloads")
        if filename:
            self.fileListDict[indx] = filename
            self.ref[indx].config(state='normal')
            self.ref[indx].delete(0, "end")
            self.ref[indx].insert(0, filename)
            self.ref[indx].config(state='disabled')

    def SubmitBtn(self):
        selected_value = self.dropdown.get()
        if selected_value == "Select an option":
            messagebox.showwarning('Warning', 'Please select an option from the dropdown')
            return

        all_files_selected = all(self.fileListDict.get(i) for i in range(self.FileBrowsCount))
        if not all_files_selected:
            messagebox.showwarning('Warning', 'Please select all files')
            return
        
        # Process the collected data, including dropdown selection
        # (Replace with actual data processing function)
        print("Selected files:", self.fileListDict)
        print("Dropdown selection:", selected_value)
        
        messagebox.showinfo('Information', 'Your data has been processed successfully.')
        self.UF.destroy()

# Initialize and run the FilePicker
app = FilePicker()
app.UF.mainloop()