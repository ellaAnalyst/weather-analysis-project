import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('scripts/weather.csv')

# Convert necessary columns to numeric, assuming they are not already
data['Temp9am'] = pd.to_numeric(data['Temp9am'], errors='coerce')
data['Temp3pm'] = pd.to_numeric(data['Temp3pm'], errors='coerce')
data['WindSpeed9am'] = pd.to_numeric(data['WindSpeed9am'], errors='coerce')
data['WindSpeed3pm'] = pd.to_numeric(data['WindSpeed3pm'], errors='coerce')

# Creating box plots for temperature at 9 AM and 3 PM
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot(data['Temp9am'].dropna())
plt.title('Box Plot for Temperature at 9 AM')
plt.xlabel('Temperature (°C)')

plt.subplot(1, 2, 2)
plt.boxplot(data['Temp3pm'].dropna())
plt.title('Box Plot for Temperature at 3 PM')
plt.xlabel('Temperature (°C)')

plt.tight_layout()
plt.show()

# Repeat the process for Wind Speed at 9 AM and 3 PM
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.boxplot(data['WindSpeed9am'].dropna())
plt.title('Box Plot for Wind Speed at 9 AM')
plt.xlabel('Wind Speed (km/h)')

plt.subplot(1, 2, 2)
plt.boxplot(data['WindSpeed3pm'].dropna())
plt.title('Box Plot for Wind Speed at 3 PM')
plt.xlabel('Wind Speed (km/h)')

plt.tight_layout()
plt.show()
