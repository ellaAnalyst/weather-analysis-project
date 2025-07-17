# 🌦️ Weather Data Analytics & Rainfall Prediction

> A full-cycle weather analytics project performing **EDA**, **clustering**, and **rainfall prediction** using machine learning models.  
> Focused on extracting actionable insights from real-world weather data to support forecasting and decision-making.

---

## 📊 Project Overview

This project analyzes Australian weather data to explore statistical patterns, discover latent weather clusters, and predict rainfall using various machine learning models.  
It simulates a professional data science workflow from raw data analysis to trained model delivery.

---

## 🎯 Objectives

- Perform structured EDA and pattern analysis
- Engineer features for improved model learning
- Apply **KMeans clustering** for weather condition discovery
- Develop classifiers to predict **RainTomorrow (Yes/No)**
- Compare models and select the best-performing model
- Generate insights applicable to **agriculture, energy, and weather forecasting**

---

## 📂 Repository Structure

| Folder / File                 | Description                                          |
|-------------------------------|------------------------------------------------------|
| `notebooks/`                  | Main analysis notebooks (`01`, `02`)                 |
| `scripts/`                    | Python modules for reusable data processing code     |
| `models/`                     | Final trained ML model (`.pkl` file)                 |
| `figures/`                    | Visual outputs (EDA, clustering, modeling)           |
| `reports/`                    | PDF project reports summarizing analysis steps       |
| `requirements.txt`            | Python dependencies                                  |
| `README.md`                   | This project overview                                |

---

## 🧩 Dataset Description

- **Source:** Australian Bureau of Meteorology (BOM)
- **Period:** March 2008 – June 2017
- **Total Records:** 1,769 daily observations
- **Target Variable:** `RainTomorrow` (Yes/No)
- **Features Include:**  
  Temperatures, wind speeds, humidity, rainfall, pressure, cloud cover, derived ratios.

---

## 🔍 Analysis & Modeling Workflow

### 🧪 01. Exploratory Analysis & Weather Pattern Clustering

- Handling missing values via median/mode imputation
- Feature engineering:
  - Binning, normalization, discretization, binarization
- Correlation analysis to identify predictive variables
- **KMeans clustering** to discover weather patterns

📄 Notebook: `01_eda_clustering.ipynb`  
📄 Report: `reports/01_eda_clustering.pdf`

---

### ☔️ 02. Rainfall Prediction Modeling

- Binary classification pipeline:
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Random Forest
  - Support Vector Machine (SVM)
  - **Neural Network (final model)**
- Evaluation metrics:
  - Accuracy, Precision, Recall, F1-Score
- Hyperparameter tuning via Grid Search & Cross-Validation
- **Neural Network** selected as final model based on:
  - Highest **accuracy (87%)**
  - Best **F1-Score (88%)**
  - Balanced performance across metrics
  - Strong generalization and overfitting resistance

📄 Notebook: `02_rain_prediction_modeling.ipynb`  
📄 Report: `reports/02_rain_prediction_modeling.pdf`

---

## 📊 Key Results & Visualizations

### 📈 Model Performance Comparison

<img src="images/modeling/Picture18.png" width="600">

> Performance of all models across Accuracy, Precision, Recall, and F1-Score.

---

### 🎯 Final Model Confusion Matrix (Neural Network)

<img src="images/modeling/Picture17.png" width="500">

> Confusion matrix of the Neural Network, showing strong prediction performance.

---

## 📊 Final Results Summary

| Model             | Accuracy | F1-Score |
|-------------------|----------|----------|
| Decision Tree     | 85%      | 85%      |
| Random Forest     | 86%      | 86%      |
| SVM               | 86%      | 86%      |
| 🌟 Neural Network | **87%**  | **88%**  |

✔️ **Final Model Selected:** Neural Network  
✔️ **Saved Model File:** `models/final_rain_prediction_model.pkl`

---

## 💡 Insights & Applications

- 📊 Afternoon **humidity** and **wind gusts** are key rainfall predictors.
- 🌦️ Clustering identified distinct weather patterns beyond nominal categories.
- 💧 Practical use cases:
   - Agricultural water planning
   - Flood risk management
   - Renewable energy optimization
   - General weather forecasting

---

## ⚙️ Tech Stack

- **Languages:** Python 3.x, Jupyter Notebook
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
- **Outputs:** PDF reports, trained ML model, visualizations

---

## 📦 Project Deliverables

- 📊 EDA-driven insights with statistical and correlation analysis
- 🌀 Weather condition clustering using KMeans
- ☔️ Rain prediction classifier (Neural Network)
- 📈 Visualized model comparisons and confusion matrix
- 📄 PDF reports summarizing analysis steps
- 📁 Trained prediction model for future deployment

---

<p align="center">
  📊 EDA ➔ 🛠️ Feature Engineering ➔ 🌀 Clustering ➔ 🤖 ML Modeling ➔ 📈 Insights
</p>

---

## ✅ Why This Project Matters

This project showcases a **professional-grade, end-to-end machine learning workflow**, transitioning from data exploration to actionable prediction. It highlights my ability to handle raw data, design features, build interpretable models, and deliver practical, deployable solutions — essential competencies for data science roles.
