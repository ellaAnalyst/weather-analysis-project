import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# 데이터 로딩
data = pd.read_csv('scripts/weather.csv') 

# 클러스터링에 사용할 변수 선택
temp_data = data[['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm']]

# NaN 값 제거 (필요한 경우)
temp_data.dropna(inplace=True)

# KMeans 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=0).fit(temp_data)
temp_data['Cluster'] = kmeans.labels_

# 클러스터링 결과 시각화
sns.pairplot(temp_data, hue='Cluster', vars=['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm'])
plt.suptitle('Temperature Clustering', size=16)
plt.show()

# 습도와 온도 클러스터링
humidity_temp_data = data[['Humidity9am', 'Temp9am', 'Humidity3pm', 'Temp3pm']]

# NaN 값 제거
humidity_temp_data.dropna(inplace=True)

# KMeans 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=0).fit(humidity_temp_data)
humidity_temp_data['Cluster'] = kmeans.labels_

# 클러스터링 결과 시각화
sns.pairplot(humidity_temp_data, hue='Cluster', vars=['Humidity9am', 'Temp9am', 'Humidity3pm', 'Temp3pm'])
plt.suptitle('Humidity and Temperature Clustering', size=16)
plt.show()



# 바람 속도 클러스터링
wind_data = data[['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm']]

# NaN 값 제거
wind_data.dropna(inplace=True)

# KMeans 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=0).fit(wind_data)
wind_data['Cluster'] = kmeans.labels_

# 클러스터링 결과 시각화
sns.pairplot(wind_data, hue='Cluster', vars=['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm'])
plt.suptitle('Wind Speed Clustering', size=16)
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

data = pd.read_csv('scripts/weather.csv')

temp_data = data[['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm']]
temp_data.dropna(inplace=True)
kmeans = KMeans(n_clusters=3, random_state=0).fit(temp_data)
temp_data['Cluster'] = kmeans.labels_
sns.pairplot(temp_data, hue='Cluster', vars=['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm'])
plt.suptitle('Temperature Clustering', size=16)
plt.show()

humidity_temp_data = data[['Humidity9am', 'Temp9am', 'Humidity3pm', 'Temp3pm']]
humidity_temp_data.dropna(inplace=True)
kmeans = KMeans(n_clusters=3, random_state=0).fit(humidity_temp_data)
humidity_temp_data['Cluster'] = kmeans.labels_
sns.pairplot(humidity_temp_data, hue='Cluster', vars=['Humidity9am', 'Temp9am', 'Humidity3pm', 'Temp3pm'])
plt.suptitle('Humidity and Temperature Clustering', size=16)
plt.show()

wind_data = data[['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm']]
wind_data.dropna(inplace=True)
kmeans = KMeans(n_clusters=3, random_state=0).fit(wind_data)
wind_data['Cluster'] = kmeans.labels_
sns.pairplot(wind_data, hue='Cluster', vars=['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm'])
plt.suptitle('Wind Speed Clustering', size=16)
plt.show()