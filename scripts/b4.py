import pandas as pd

# data road
data = pd.read_csv('14502431.csv') 
# Binarization condition example: Binarize based on whether the wind direction is north
# Assuming 'N', 'NNE', 'NE', 'ENE' are considered '1' and others are '0'
north_directions = ['N', 'NNE', 'NE', 'ENE']
data['WindDir9am_Binary'] = data['WindDir9am'].apply(lambda x: 1 if x in north_directions else 0)

# result print
print(data[['WindDir9am', 'WindDir9am_Binary']].head())
