import pandas as pd

# Sample DataFrame
data = {
    'fund': ['FundA', 'FundA', 'FundB', 'FundB', 'FundC'],
    'client_earnings': [100, 150, 200, 250, 300],
    'net_earnings': [90, 140, 180, 230, 270],
    'borrower': ['John', 'Jane', 'Alice', 'Bob', 'Charlie']
}

df = pd.DataFrame(data)

# Step 1: Group by fund and sum the earnings
grouped_df = df.groupby('fund').agg({
    'client_earnings': 'sum',
    'net_earnings': 'sum'
}).reset_index()

# Step 2: Concatenate all borrowers for each fund
borrower_df = df.groupby('fund')['borrower'].apply(lambda x: ', '.join(x)).reset_index()

# Step 3: Merge the borrower data back into the grouped DataFrame
result_df = pd.merge(grouped_df, borrower_df, on='fund', how='left')

# Display the result
print(result_df)