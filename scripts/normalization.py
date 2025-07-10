import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('14502431.csv')  # Modify the file path as needed

# Apply Min-Max Normalization
data['MaxTemp_MinMax'] = (data['MaxTemp'] - data['MaxTemp'].min()) / (data['MaxTemp'].max() - data['MaxTemp'].min())

# Visualize the result of Min-Max Normalization
plt.figure(figsize=(8, 4))
plt.hist(data['MaxTemp_MinMax'], bins=30, color='blue', alpha=0.7)
plt.title('Min-Max Normalization of MaxTemp')
plt.xlabel('Normalized MaxTemp')
plt.ylabel('Frequency')
plt.show()

# Apply Z-score Normalization
data['MaxTemp_Zscore'] = (data['MaxTemp'] - data['MaxTemp'].mean()) / data['MaxTemp'].std()

# Visualize the result of Z-score Normalization
plt.figure(figsize=(8, 4))
plt.hist(data['MaxTemp_Zscore'], bins=30, color='green', alpha=0.7)
plt.title('Z-score Normalization of MaxTemp')
plt.xlabel('Z-score Normalized MaxTemp')
plt.ylabel('Frequency')
plt.show()
