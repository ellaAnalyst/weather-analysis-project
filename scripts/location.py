import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# CSV 파일 로드
df = pd.read_csv('14502431.csv')

# 날짜 데이터를 datetime 타입으로 변환
df['Date'] = pd.to_datetime(df['Date'])

# 지역별 데이터 수 계산
location_counts = df['Location'].value_counts()
print(location_counts)

# Matplotlib을 이용한 시각화
plt.figure(figsize=(10, 8))
location_counts.plot(kind='bar')
plt.title('Frequency of Data by Location')
plt.xlabel('Location')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

