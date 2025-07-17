# 🌦️ Weather Data Analytics & Rainfall Prediction

> A full-cycle weather analytics project performing EDA, clustering, and rainfall prediction using machine learning.  
> Focused on transforming raw weather data into actionable insights and predictive solutions.

---

## 📊 Project Overview

This project analyzes Australian weather data to discover hidden weather patterns and build a rainfall prediction model using supervised machine learning techniques.  
It simulates a professional data science pipeline from exploratory analysis to model development and result delivery.

---

## 🎯 Objectives

- Discover statistical and environmental patterns using EDA
- Engineer features from raw weather data for improved modeling
- Identify latent weather condition clusters via KMeans
- Predict rainfall (`RainTomorrow`) using various classifiers
- Evaluate models and justify the final model selection
- Generate insights applicable to real-world planning and forecasting

---

## 📂 Repository Structure

| Folder / File                 | Description                                          |
|-------------------------------|------------------------------------------------------|
| `notebooks/`                  | Main analysis notebooks                              |
| `scripts/`                    | Modular Python scripts for data processing & modeling |
| `models/`                     | Trained ML model (saved `.pkl`)                      |
| `figures/`                    | Visual outputs (EDA, clustering, modeling)           |
| `reports/`                    | PDF reports summarizing analysis steps               |
| `requirements.txt`            | Python dependencies                                  |
| `README.md`                   | Project overview and key results                     |

---

## 🧩 Dataset Description

- **Source:** Australian Bureau of Meteorology (BOM)
- **Period:** 2008 – 2017
- **Total Records:** 1,769 days
- **Target Variable:** `RainTomorrow` (Yes/No)
- **Features:**  
  Temperatures, wind speeds, humidity, rainfall, pressure, cloud cover, and engineered ratios.

---

## 🔍 Analysis Flow

### 🧪 01. Exploratory Analysis & Weather Pattern Clustering

- Missing data analysis and handling
- Feature engineering:
  - Binning, normalization, discretization, binarization
- Correlation analysis between weather features
- **KMeans clustering** applied to discover underlying weather conditions beyond nominal categories

📄 Notebook: `01_eda_clustering.ipynb`  
📄 Report: `reports/01_eda_clustering.pdf`

---

### ☔️ 02. Rainfall Prediction Modeling

- Supervised ML pipeline using:
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Random Forest
  - Support Vector Machine (SVM)
  - **Neural Network (Final Model)**
- Model evaluation via accuracy, precision, recall, F1-Score
- Final model selected based on **robustness and performance across all metrics**

📄 Notebook: `02_rain_prediction_modeling.ipynb`  
📄 Report: `reports/02_rain_prediction_modeling.pdf`

---

## 📈 Key Visualizations

### 📊 Model Performance Comparison

<img src="images/modeling/Picture18.png" width="600">

> Performance comparison across all classifiers using Accuracy, Precision, Recall, and F1-Score.

---

### 🎯 Final Model Confusion Matrix (Neural Network)

<img src="images/modeling/Picture17.png" width="500">

> Neural Network confusion matrix showing final classification performance.

---

## 📊 Final Results Summary

| Model             | Accuracy | F1-Score |
|-------------------|----------|----------|
| Decision Tree     | 85%      | 85%      |
| Random Forest     | 86%      | 86%      |
| SVM               | 86%      | 86%      |
| 🌟 Neural Network | **87%**  | **88%**  |

✔️ **Final Model:** Neural Network  
✔️ **Saved Model:** `models/final_rain_prediction_model.pkl`

> Neural Network was selected as the final model due to its superior generalization performance and consistent F1-Score, despite the interpretability trade-off.

---

## 💡 Key Insights

- 📊 **Wind gusts** and **afternoon humidity** emerged as critical rainfall predictors.
- 🌦️ KMeans clustering revealed distinguishable weather conditions not evident in raw categorical variables.
- 🚜 This pipeline can support **agricultural water management**, energy planning, and **flood risk monitoring**.

---

## ⚙️ Tech Stack

- **Python 3.x, Jupyter Notebook**
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
- **Outputs:** Visualizations, trained model, reports

---

## 📦 Deliverables

- EDA-driven insights and correlation analysis
- Weather condition clustering (KMeans)
- Rainfall prediction classifier (Neural Network)
- Visualized performance comparisons and confusion matrix
- PDF reports summarizing each step
- Trained prediction model (Neural Network) for deployment

---

<p align="center">
  📊 EDA ➔ 🛠️ Feature Engineering ➔ 🌀 Clustering ➔ 🤖 ML Modeling ➔ 📈 Insights
</p>
