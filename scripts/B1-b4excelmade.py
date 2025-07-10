import pandas as pd

# Load the data
data = pd.read_csv('14502431.csv')

# Task B1: Equi-width and Equi-depth Binning of 'Rainfall'
data['Rainfall_EquiWidth'] = pd.cut(data['Rainfall'], bins=5, labels=False)
data['Rainfall_EquiDepth'] = pd.qcut(data['Rainfall'], q=5, duplicates='drop', labels=False)

# Task B2: Normalization of 'MaxTemp'
data['MaxTemp_MinMax'] = (data['MaxTemp'] - data['MaxTemp'].min()) / (data['MaxTemp'].max() - data['MaxTemp'].min())
data['MaxTemp_Zscore'] = (data['MaxTemp'] - data['MaxTemp'].mean()) / data['MaxTemp'].std()

# Task B3: Discretization of 'WindSpeed3pm'
bins = [0, 15, 30, 45, data['WindSpeed3pm'].max()]
labels = ['Slow', 'Moderate', 'Fast', 'Very Fast']
data['WindSpeed3pm_Discrete'] = pd.cut(data['WindSpeed3pm'], bins=bins, labels=labels)

# Task B4: Binarization of 'WindDir9am'
north_directions = ['N', 'NNE', 'NE', 'ENE']
data['WindDir9am_Binary'] = data['WindDir9am'].apply(lambda x: 1 if x in north_directions else 0)

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('Preprocessed_Weather_Data.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet
data[['Rainfall', 'Rainfall_EquiWidth', 'Rainfall_EquiDepth']].to_excel(writer, sheet_name='B1_Smoothing_Rainfall', index=False)
data[['MaxTemp', 'MaxTemp_MinMax', 'MaxTemp_Zscore']].to_excel(writer, sheet_name='B2_Normalization_MaxTemp', index=False)
data[['WindSpeed3pm', 'WindSpeed3pm_Discrete']].to_excel(writer, sheet_name='B3_Discretization_WindSpeed', index=False)
data[['WindDir9am', 'WindDir9am_Binary']].to_excel(writer, sheet_name='B4_Binarization_WindDir', index=False)


# Close the Pandas Excel writer and output the Excel file
writer.close()
