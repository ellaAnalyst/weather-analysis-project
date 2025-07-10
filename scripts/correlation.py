import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv('scripts/weather.csv')

# Exclude non-numeric columns
numeric_data = data.select_dtypes(include=[np.number])

# Calculate the Pearson correlation coefficients
correlation_matrix = numeric_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm',
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

# Add titles and labels
plt.title('Linear Correlation Matrix Heatmap')
plt.xlabel('Variables')
plt.ylabel('Variables')

# Show plot
plt.show()
