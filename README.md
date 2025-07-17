# 🌦️ Weather Data Analytics & Rainfall Prediction

> A practical, end-to-end weather data project covering **exploratory analysis**, **feature engineering**, **clustering**, and **rainfall prediction using machine learning models**.

---

## 📊 Project Overview

This project explores Australian weather data to build an end-to-end analysis and modeling workflow.  
Starting from data understanding and pattern discovery, it culminates in a trained machine learning model capable of predicting whether it will rain tomorrow.

The goal is to simulate a professional data analysis pipeline from raw data to actionable predictions.

---

## 🎯 Objectives

- Explore statistical structures of weather data through EDA
- Apply preprocessing techniques:
  - Binning, normalization, discretization, binarization
- Discover weather condition patterns using KMeans clustering
- Predict rainfall (`RainTomorrow`) using supervised classifiers
- Compare model performances and select the best one
- Generate practical insights for weather-based decisions

---

## 📂 Repository Structure

| Folder / File                 | Description                                          |
|-------------------------------|------------------------------------------------------|
| `notebooks/`                  | Analysis notebooks (EDA, clustering, modeling)       |
| ├── 01_eda_clustering.ipynb   | Exploratory analysis, preprocessing, clustering      |
| └── 02_rain_prediction_modeling.ipynb | Machine learning classification pipeline      |
| `scripts/`                    | Python modules for preprocessing and modeling        |
| `models/`                     | Final trained prediction model (.pkl)                |
| `figures/`                    | Output visualizations (EDA, clustering, modeling)    |
| `reports/`                    | PDF reports summarizing each pipeline step           |
| `requirements.txt`            | Python dependencies                                  |
| `README.md`                   | Project overview and documentation                   |

---

## 🧩 Dataset Description

- **Source:** Australian Bureau of Meteorology (BOM)  
- **Time Period:** March 2008 – June 2017  
- **Total Entries:** 1,769 days  
- **Features:**  
  - Temperatures (MinTemp, MaxTemp, Temp9am, Temp3pm)
  - Wind speeds (Gust, 9am, 3pm)
  - Humidity, Rainfall, Sunshine, CloudCover, Pressure
  - Binary conditions: Bio presence, Profile picture presence
  - Derived features: Follow Ratio, Post Ratio
- **Target:** `RainTomorrow` (Yes/No)

---

## 🔍 Analysis Flow

### 🧪 01. EDA & Weather Pattern Clustering

- Data cleaning and missing value analysis
- Feature engineering:
  - Binning, normalization, discretization, binarization
- Correlation analysis between weather attributes
- KMeans clustering:
  - Grouping weather conditions by temperature, wind, and humidity
- Visualization of patterns and clusters

📄 Detailed in:  
- Notebook: `01_eda_clustering.ipynb`  
- Report: `reports/01_eda_clustering.pdf`

---

### ☔️ 02. Rain Prediction Modeling

- Predicting next-day rainfall using ML classifiers
- Workflow:
  - Data preprocessing and feature selection
  - Train/validation/test splitting
  - Models compared:
    - Decision Tree
    - K-Nearest Neighbors
    - Random Forest
    - Support Vector Machine (SVM)
    - Neural Network (**final model**)
  - Model evaluation using accuracy and F1-score
  - Final model selected based on stability and performance

📄 Detailed in:  
- Notebook: `02_rain_prediction_modeling.ipynb`  
- Report: `reports/02_rain_prediction_modeling.pdf`

---

## 📈 Final Results

| Model                 | Accuracy | F1-Score |
|-----------------------|----------|----------|
| Decision Tree         | 85%      | 85%      |
| Random Forest         | 86%      | 86%      |
| SVM                   | 86%      | 86%      |
| 🌟 Neural Network     | **87%**  | **88%**  |

✔️ **Final Model:** Neural Network  
✔️ **Trained Model Saved:**  
`models/final_rain_prediction_model.pkl`

---

## ⚙️ Tech Stack

- **Languages:** Python 3.x, Jupyter Notebook  
- **Libraries:** pandas, numpy, scikit-learn, seaborn, matplotlib  
- **Tools:** Modular Python scripts, visual reporting

---

## 📦 Deliverables

- 📊 Weather condition clustering model (KMeans)
- ☔️ Rainfall prediction model (Neural Network)
- 📈 Visual reports (EDA, clustering, modeling)
- 📄 PDF reports summarizing analysis steps
- 📁 Ready-to-use trained model (.pkl)

---

<p align="center">
  📊 Data analysis ➔ 🛠️ Feature engineering ➔ 🤖 ML modeling ➔ 📈 Insight
</p>
