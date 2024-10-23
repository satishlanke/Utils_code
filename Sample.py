from datetime import datetime

def get_target_date():
    # Get the current date and year
    today = datetime.today()
    current_year = today.year
    
    # Define April 30 and October 31 with the current year
    april_30 = datetime(current_year, 4, 30)
    october_31 = datetime(current_year, 10, 31)
    
    # Check the month and decide which date to pick
    if today.month in [4, 5, 6]:  # Between April and June
        return april_30
    elif today.month in [10, 11, 12]:  # Between October and December
        return october_31
    else:
        return today  # If not in the specified ranges, return today's date

# Call the function and print the result
target_date = get_target_date()
print(f"The target date is: {target_date.strftime('%m/%d/%Y')}")