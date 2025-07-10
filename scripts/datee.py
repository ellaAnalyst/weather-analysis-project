import pandas as pd

# Load the dataset from the specified file path
data = pd.read_csv('14502431.csv')

# Convert the 'Date' column to datetime format for easier analysis
data['Date'] = pd.to_datetime(data['Date'])

# Calculate basic date information
total_days_recorded = data['Date'].nunique()
oldest_date = data['Date'].min()
newest_date = data['Date'].max()
date_range = newest_date - oldest_date

# Additional insights: frequency of data collection per year
yearly_frequency = data['Date'].dt.year.value_counts().sort_index()

# Print the results
print("Total Days Recorded:", total_days_recorded)
print("Date Range:", date_range.days, "days")
print("Oldest Date:", oldest_date.strftime('%Y-%m-%d'))
print("Newest Date:", newest_date.strftime('%Y-%m-%d'))
print("\nData Collection Frequency per Year:")
print(yearly_frequency)

# Optionally, save these results to a text file for reference
with open('date_analysis_summary.txt', 'w') as file:
    file.write(f"Total Days Recorded: {total_days_recorded}\n")
    file.write(f"Date Range: {date_range.days} days\n")
    file.write(f"Oldest Date: {oldest_date.strftime('%Y-%m-%d')}\n")
    file.write(f"Newest Date: {newest_date.strftime('%Y-%m-%d')}\n")
    file.write("\nData Collection Frequency per Year:\n")
    file.write(str(yearly_frequency))
