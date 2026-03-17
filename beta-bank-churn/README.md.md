# 🏦 Beta Bank Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-green?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Approved%20✅-brightgreen?style=flat-square)
![TripleTen](https://img.shields.io/badge/TripleTen-Data%20Analytics-purple?style=flat-square)

---

## 📌 Project Overview

Beta Bank is losing customers — and retaining existing customers is significantly cheaper than acquiring new ones. This project builds a **supervised machine learning classification model** to predict whether a customer will leave the bank (churn), enabling the business to proactively intervene with at-risk customers.

**Business Goal:** Predict customer churn with an F1 score ≥ 0.59 on the test set.

**Result Achieved:** ✅ **F1 = 0.637 | ROC-AUC = 0.869**

---

## 📂 Repository Structure

```
beta-bank-churn/
│
├── data/
│   └── Churn.csv               # Customer data (10,000 records)
│
├── notebook/
│   └── beta_bank_churn.ipynb   # Full analysis & modeling notebook
│
├── images/
│   └── (visualizations)        # Charts referenced in this README
│
└── README.md
```

---

## 📊 Dataset

| Feature | Description |
|---|---|
| `CreditScore` | Customer's credit score |
| `Geography` | Country (France, Germany, Spain) |
| `Gender` | Male / Female |
| `Age` | Customer age |
| `Tenure` | Years as a bank customer |
| `Balance` | Account balance |
| `NumOfProducts` | Number of bank products used |
| `HasCrCard` | Has a credit card (1 = Yes) |
| `IsActiveMember` | Active account status (1 = Yes) |
| `EstimatedSalary` | Estimated annual salary |
| **`Exited`** | **Target — 1 = Churned, 0 = Stayed** |

**Dataset size:** 10,000 rows × 14 columns

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Filled missing values in `Tenure` with the **median** (robust to outliers)
- Dropped non-informative identifier columns: `RowNumber`, `CustomerId`, `Surname`
- Applied **One-Hot Encoding** to `Geography` and `Gender`
- Split into **Train / Validation / Test (60/20/20)** with stratified sampling to preserve class ratios
- Applied **StandardScaler** (fit on train only, applied to all sets)

### 2. Class Imbalance Analysis
The target variable was found to be significantly imbalanced:

| Class | Proportion |
|---|---|
| 0 — Stayed | ~79.6% |
| 1 — Churned | ~20.4% |

Training on imbalanced data causes models to favor the majority class, resulting in poor recall on churned customers — the class that matters most for business action.

### 3. Imbalance Handling Strategies

Two approaches were tested and compared:

- **Upsampling** — The minority class (Exited = 1) was resampled with replacement to match the size of the majority class, creating a balanced 50/50 training set
- **class_weight='balanced'** — Models were trained with automatic class weights, penalizing misclassification of the minority class more heavily in the loss function

### 4. Models Trained

| Model | Strategy | F1 Score | ROC-AUC |
|---|---|---|---|
| Logistic Regression | Imbalanced (baseline) | 0.531 | 0.872 |
| Random Forest | Imbalanced (baseline) | — | — |
| Logistic Regression | Upsampled | 0.626 | 0.871 |
| Random Forest | Upsampled | **0.626+** | 0.871 |
| Logistic Regression | class_weight balanced | 0.639 | 0.867 |
| Random Forest | class_weight balanced | **Best validation** | 0.869 |

### 5. Hyperparameter Tuning
Grid search over `max_depth` ∈ {6, 8, 10, 12} and `n_estimators` ∈ {50, 100, 200, 300} using F1 score on the validation set. Best configuration was selected and retrained on the full train+validation set before final test evaluation.

---

## 🏆 Final Test Results

The final model — **Random Forest with upsampling** — was evaluated on the held-out test set:

```
Final F1:       0.637
Final ROC-AUC:  0.869

              precision    recall  f1-score   support

           0       0.92      0.86      0.89      1593
           1       0.57      0.72      0.64       407

    accuracy                           0.83      2000
```

**Key Takeaway:** The model correctly identifies **72% of customers who actually churn** (recall = 0.72), giving Beta Bank the ability to target retention efforts where they matter most.

---

## 🔍 Key Findings

- The dataset had a significant class imbalance (~80/20 split) — training without addressing this led to models that mostly ignored churned customers
- Both upsampling and class_weight balancing improved F1 substantially over the baseline
- **Random Forest consistently outperformed Logistic Regression**, especially after balancing
- The final model exceeds the project threshold (F1 ≥ 0.59) with **F1 = 0.637** and **ROC-AUC = 0.869**
- A ROC-AUC of 0.869 means the model has strong discriminatory power — it ranks churning customers above staying customers ~87% of the time

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Core language |
| Pandas | Data loading & manipulation |
| NumPy | Numerical operations |
| scikit-learn | Modeling, preprocessing, metrics |
| Jupyter Notebook | Development environment |

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/beta-bank-churn.git
cd beta-bank-churn
```

**2. Install dependencies**
```bash
pip install pandas numpy scikit-learn jupyter
```

**3. Launch the notebook**
```bash
jupyter notebook notebook/beta_bank_churn.ipynb
```

**4. Run all cells**  
In Jupyter: `Kernel → Restart & Run All`

> **Note:** The dataset (`Churn.csv`) is included in the `data/` folder. If the notebook path doesn't match, update the `pd.read_csv()` path in Cell 2 to `'../data/Churn.csv'`.

---

## 👤 Author

**Marc (Ayebi)**  
U.S. Navy Veteran → Data Analyst  
TripleTen Data Analytics Bootcamp


---

## 📝 Project Status

✅ **Approved by TripleTen reviewer** — All feedback addressed across two review rounds.  
Reviewer comment: *"Amazing job with this submission! Everything looks much more complete now."*
