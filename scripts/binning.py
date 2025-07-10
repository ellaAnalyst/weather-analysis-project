import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('14502431.csv')  # Adjust the file path as needed


# Equi-width Binning - Set the number of bins
bin_count = 5

# Apply Equi-width Binning
data['Rainfall_EquiWidth'] = pd.cut(data['Rainfall'], bins=bin_count, labels=False)

# Visualize the result of Equi-width Binning
plt.figure(figsize=(8, 4))
data['Rainfall_EquiWidth'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Equi-width Binning of Rainfall')
plt.xlabel('Bins')
plt.ylabel('Count')
plt.show()

# Apply Equi-depth Binning
try:
    data['Rainfall_EquiDepth'] = pd.qcut(data['Rainfall'], q=bin_count, duplicates='drop', labels=False)
except ValueError as e:
    print("Error:", e)
    print("Not enough unique values to create the requested number of bins. Consider reducing the number of bins or adjusting the data.")

# Visualize the result of Equi-depth Binning
plt.figure(figsize=(8, 4))
data['Rainfall_EquiDepth'].value_counts().sort_index().plot(kind='bar', color='green')
plt.title('Equi-depth Binning of Rainfall')
plt.xlabel('Bins')
plt.ylabel('Count')
plt.show()
