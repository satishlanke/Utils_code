import xlwings as xw
import pandas as pd

# Sample DataFrame
data = {'A': ['short', 'this is longer text', 'medium', 'tiny'], 
        'B': [5, 1234567890, 7, 8], 
        'C': ['small', 'text with spaces', 'longer text', 'mid']}
df = pd.DataFrame(data)

# Start an Excel app instance
wb = xw.Book()  # Open a new workbook
sheet = wb.sheets['Sheet1']  # Select the active sheet

# Static sentences in the first few rows
static_sentences = ["This is static sentence 1",
                    "This is static sentence 2",
                    "This is static sentence 3",
                    "This is static sentence 4"]

# Write all static sentences at once, starting from cell A1
sheet.range('A1:A4').value = [[sentence] for sentence in static_sentences]

# Dynamically calculate the starting row based on static content
start_row = len(static_sentences) + 1  # This will be 5 (after the static content)

# Write the DataFrame starting from F{start_row}, excluding the index
sheet.range(f'F{start_row}').value = df.values  # Write DataFrame without index

# Optionally, write the column headers at row {start_row - 1}
sheet.range(f'F{start_row - 1}').value = df.columns.tolist()

# Autofit the columns where the DataFrame is written (starting from column F)
sheet.range(f'F{start_row - 1}:H{start_row + len(df) - 1}').columns.autofit()  # Adjust columns F to H based on data

# Set Arial font for the entire sheet
sheet.cells.api.Font.Name = 'Arial'

# Example: Insert data into a specific cell (row number 10, column 'C') and make it bold
row_number = 10
cell_value = "This is bold text"
sheet.range(f'C{row_number}').value = cell_value  # Insert data
sheet.range(f'C{row_number}').api.Font.Bold = True  # Make the font bold

# Save the workbook
wb.save('output.xlsx')
wb.close()