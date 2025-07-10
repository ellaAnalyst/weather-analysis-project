# 🌦️ Weather Data Analytics: EDA, Preprocessing & Clustering

> A full-cycle portfolio project for practical data analysis using weather data  
> Covers EDA → Preprocessing → Visualization → Clustering with professional depth

---

## 📌 Project Overview

This project explores Australian weather data to perform end-to-end data analysis, including **attribute identification, preprocessing, exploratory visualization, correlation analysis, and clustering**.  
The focus is on building a well-structured, interpretable analysis flow that prepares data for modeling and decision-making in real-world applications.

- Exploratory and statistical insights from raw climate data  
- Multiple data preprocessing methods applied for structure and clarity  
- K-Means clustering to group weather patterns by temperature, wind, and humidity

---

## 🎯 Objectives

- Understand the statistical structure and attributes of weather data  
- Apply preprocessing techniques (Binning, Normalization, etc.) to prepare data  
- Analyze inter-variable correlations with visual interpretation  
- Use **KMeans clustering** to classify similar weather conditions  
- Generate actionable insights applicable to real-world domains

---

## 🔍 Dataset Description

- **Source:** Australian Bureau of Meteorology (BOM)  
- **Period:** March 10, 2008 – June 22, 2017  
- **Entries:** 1,769 recorded days  
- **Variables include:**  
  - Temperatures (MinTemp, MaxTemp, Temp9am, Temp3pm)  
  - Wind (WindGustSpeed, WindSpeed9am, WindSpeed3pm)  
  - Humidity, Pressure, Rainfall, Sunshine, CloudCover, etc.  
- **Types:** Mixed (Nominal, Ordinal, Interval, Ratio)

---

## ⚙️ Tech Stack

- **Language & Environment:** Python 3.x, Jupyter Notebook  
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn  
- **Structure:** `.ipynb` for main flow, `.py` for modular functions

---

## 🗂️ Project Structure

weather-data-analytics/
├── notebooks/ # Main analysis steps (EDA, Preprocessing, Clustering)
├── scripts/ # Python modules for reusable logic
├── images/ # Output plots and visualizations
├── report/ # Final report (PDF)
├── README.md
├── requirements.txt
└── .gitignore



---

## 📊 Analysis Summary

### 🧪 1. Exploratory Data Analysis (EDA)
- Visualize and describe distribution across key variables  
- Identify data gaps, outliers, and value ranges  
- Pearson Correlation Matrix:  
  - Strong positive correlations between temperatures  
  - Negative correlations between temperature and humidity

### 🧹 2. Preprocessing
- **Binning:** Applied both equi-width and equi-depth binning to Rainfall  
- **Normalization:** MaxTemp normalized using Min-Max and Z-score  
- **Discretization:** WindSpeed3pm categorized into ‘Slow’ to ‘Very Fast’  
- **Binarization:** WindDir9am converted into binary (N-direction = 1, else = 0)

### 📈 3. Clustering (KMeans)
- **Temperature clustering:** Clear grouping between morning lows and afternoon highs  
- **Wind clustering:** Separated high gust days from moderate conditions  
- **Humidity-Temperature clustering:** Identified dry/hot vs. humid/cool clusters  
- **Application:** Useful for weather modeling, energy planning, and agriculture

---

## 💡 Key Findings

- Daily temperature patterns are highly predictable → usable for energy demand forecasting  
- Rainfall mostly absent → indicates dry climate or seasonal precipitation  
- Wind speeds higher in the afternoon → relevant for wind energy strategy  
- Clustering reveals consistent weather types (e.g. hot-dry, humid-cool days)

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/gosarii/weather-data-analytics.git
cd weather-data-analytics

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install required libraries
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
