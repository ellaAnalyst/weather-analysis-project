import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('14502431.csv')  # Update the path to your CSV file

# Count the occurrences of 'Yes' and 'No' for 'RainToday'
rain_today_counts = df['RainToday'].value_counts()

# Plotting RainToday
plt.figure(figsize=(8, 6))
plt.pie(rain_today_counts, labels=rain_today_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Rain Today')
plt.show()

# Count the occurrences of 'Yes' and 'No' for 'RainTomorrow'
rain_tomorrow_counts = df['RainTomorrow'].value_counts()

# Plotting RainTomorrow
plt.figure(figsize=(8, 6))
plt.pie(rain_tomorrow_counts, labels=rain_tomorrow_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Rain Tomorrow')
plt.show()
