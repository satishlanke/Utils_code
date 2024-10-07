SELECT 
    t.*, 
    subtotal.amount_subtotal
FROM 
    your_table t
JOIN 
    (SELECT 
         country_risk, 
         client_name, 
         SUM(amount) AS amount_subtotal
     FROM 
         your_table
     GROUP BY 
         country_risk, client_name) subtotal
ON 
    t.country_risk = subtotal.country_risk 
    AND t.client_name = subtotal.client_name;


import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font, Alignment
from openpyxl import Workbook

# Sample DataFrame
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
})

# Create a new Excel workbook
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Get the openpyxl workbook and sheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Format the header row
    for cell in worksheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')




import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
})

# Write DataFrame to Excel with formatting
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Get the xlsxwriter objects
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Define a format for bold header and center alignment
    header_format = workbook.add_format({'bold': True, 'align': 'center'})

    # Apply the format to the header
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)