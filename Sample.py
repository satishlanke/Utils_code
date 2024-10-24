import xlwings as xw
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Jane', 'Doe'],
        'Age': [30, 25, 22]}
df = pd.DataFrame(data)

# Create a new Excel workbook or open an existing one
wb = xw.Book()  # Create a new workbook

# Select a sheet (by default, it's 'Sheet1')
sheet = wb.sheets['Sheet1']

# Write the DataFrame headers and values without the index
sheet.range('A1').value = [df.columns.tolist()]  # Write headers
sheet.range('A2').value = df.values  # Write values without index

# Set font size to 9 for the entire DataFrame (headers + values)
total_rows = len(df) + 1  # Total rows including header
total_columns = len(df.columns)
sheet.range(f'A1:{chr(ord("A") + total_columns - 1)}{total_rows}').api.Font.Size = 9

# Find the last column and make it bold
last_col_letter = chr(ord('A') + len(df.columns) - 1)
sheet.range(f'{last_col_letter}1:{last_col_letter}{total_rows}').api.Font.Bold = True

# Save the workbook to a file
wb.save('output_font_size_9.xlsx')

# Optionally, close the workbook
wb.close()