# 📊 Data Projects — TripleTen

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![TripleTen](https://img.shields.io/badge/TripleTen-Data%20Analytics%20Bootcamp-purple?style=flat-square)
![Veteran](https://img.shields.io/badge/U.S.%20Navy-Veteran-navy?style=flat-square)

---

## 👋 About This Repository

This repository contains data analytics and machine learning projects completed as part of the **TripleTen Data Analytics Bootcamp**. Each project tackles a real-world business problem using industry-standard tools and workflows ,from data cleaning and exploratory analysis to predictive modeling and evaluation.

I'm a U.S. Navy veteran transitioning into data analytics. My military background gives me a strong foundation in precision, process, and accountability — values I bring directly into every analysis I build.

---

## 🗂️ Projects

| # | Project | Domain | Key Skills | Status |
|---|---|---|---|---|
| 01 | [Beta Bank Churn Prediction](#-project-01--beta-bank-churn-prediction) | Banking / ML | Classification, Imbalanced Data, Random Forest | ✅ Approved |

> More projects will be added as the bootcamp progresses.

---

## 🔍 Project 01 — Beta Bank Churn Prediction

**Folder:** `beta-bank-churn/`

### Business Problem
Beta Bank is experiencing customer churn. Retaining existing customers is far more cost-effective than acquiring new ones. The goal was to build a classification model that predicts whether a customer will leave the bank, enabling the business to proactively target at-risk customers with retention strategies.

**Target metric:** F1 Score ≥ 0.59

### Approach
- Cleaned and preprocessed 10,000 customer records
- Addressed significant class imbalance (~80% stayed / ~20% churned) using two strategies: **upsampling** and **class_weight balancing**
- Trained and compared **Logistic Regression** and **Random Forest** models
- Performed hyperparameter tuning (max_depth, n_estimators) on validation set
- Evaluated final model on a fully held-out test set

### Results

| Metric | Score |
|---|---|
| **F1 Score** | **0.637** ✅ |
| **ROC-AUC** | **0.869** |
| Recall (Churned) | 0.72 |
| Accuracy | 0.83 |

The final model correctly identifies **72% of customers who actually churn**, giving the bank actionable leads for its retention team.

### Tech Stack
`Python` · `Pandas` · `NumPy` · `scikit-learn` · `Jupyter Notebook`

📁 [View project folder](./beta-bank-churn/) | 📓 [View notebook](./beta-bank-churn/notebook/beta_bank_churn.ipynb)

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Languages | Python 3.8+ |
| Data Manipulation | Pandas, NumPy |
| Machine Learning | scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |
| Version Control | Git, GitHub |

---

## 📁 Repository Structure

```
data-projects-tripleten/
│
├── beta-bank-churn/
│   ├── data/
│   │   └── Churn.csv
│   ├── notebook/
│   │   └── beta_bank_churn.ipynb
│   └── README.md
│
└── README.md               ← You are here
```

---

*This repository is actively maintained and updated as new projects are completed.*
