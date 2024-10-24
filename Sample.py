import xlwings as xw
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Start an Excel app instance
wb = xw.Book()  # Open a new workbook
sheet = wb.sheets['Sheet1']  # Select the active sheet

# Static sentences in the first four rows
static_sentences = ["This is static sentence 1",
                    "This is static sentence 2",
                    "This is static sentence 3",
                    "This is static sentence 4"]

# Write static sentences in the first column (A) from row 1 to 4
for idx, sentence in enumerate(static_sentences, start=1):
    sheet.range(f'A{idx}').value = sentence

# Write the DataFrame starting from F5
sheet.range('F5').value = df

# Save the workbook
wb.save('output.xlsx')
wb.close()