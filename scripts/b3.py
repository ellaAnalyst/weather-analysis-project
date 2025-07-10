import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('14502431.csv')  

bins = [0, 15, 30, 45, data['WindSpeed3pm'].max()]
labels = ['Slow Wind', 'Moderate Wind', 'Fast Wind', 'Very Fast Wind']

data['WindSpeed3pm_Categories'] = pd.cut(data['WindSpeed3pm'], bins=bins, labels=labels, right=False)


category_counts = data['WindSpeed3pm_Categories'].value_counts().sort_index()
plt.figure(figsize=(8, 4))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Discretization of WindSpeed3pm')
plt.xlabel('Wind Speed Categories')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
