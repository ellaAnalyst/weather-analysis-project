import pandas as pd
import matplotlib.pyplot as plt

# Load your data here
df = pd.read_csv('14502431.csv')

# Assuming data is loaded into a DataFrame 'df' with columns 'WindDir9am' and 'WindDir3pm'

# Count the occurrences of each wind direction at 9am and 3pm
wind_dir_9am_counts = df['WindDir9am'].value_counts()
wind_dir_3pm_counts = df['WindDir3pm'].value_counts()

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart."""
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If the value of the bar is 0, don't put a label.
        if y_value == 0:
            continue

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create the label
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.

# Plotting WindDir9am
plt.figure(figsize=(10, 6))
ax = wind_dir_9am_counts.plot(kind='bar', color='skyblue')
plt.title('Wind Direction at 9 AM')
plt.xlabel('Direction')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
add_value_labels(ax)
plt.tight_layout()
plt.show()

# Plotting WindDir3pm
plt.figure(figsize=(10, 6))
ax = wind_dir_3pm_counts.plot(kind='bar', color='lightgreen')
plt.title('Wind Direction at 3 PM')
plt.xlabel('Direction')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
add_value_labels(ax)
plt.tight_layout()
plt.show()
