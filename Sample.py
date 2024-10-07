import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Border, Side

# Sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [28, 24, 30],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Write DataFrame to Excel with pd.ExcelWriter and openpyxl engine
with pd.ExcelWriter('output_with_lines.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Define the border style for horizontal lines
    thin_border = Border(left=Side(style='thin'),
                         right=Side(style='thin'),
                         top=Side(style='thin'),
                         bottom=Side(style='thin'))

    # Apply the border to each row
    for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=worksheet.max_column):
        for cell in row:
            cell.border = thin_border

# The file "output_with_lines.xlsx" is saved with horizontal lines between rows.