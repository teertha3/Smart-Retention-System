# Smart Retention System

A machine learning-powered web app for predicting telecom customer churn and providing actionable, rule-based retention strategies — built with **Streamlit** and **scikit-learn**.

---

## 🚀 Project Overview

Telecom companies face significant losses due to customer churn. This system helps detect potential churners in real time and suggests personalized strategies to retain them.

Key Features:
- ✅ Predicts if a customer is likely to churn based on age, gender, tenure, and monthly charges
- ✅ Displays targeted retention suggestions using a rule-based system
- ✅ Role-based login: separate access for **Admin** and **User**
- ✅ Admins can upload updated model and scaler files directly from the interface
- ✅ Built using Streamlit, trained using SVM with preprocessing and SMOTE

---

## 🧠 ML Pipeline

- Data preprocessing: encoding, scaling, SMOTE balancing
- Model: Support Vector Machine (SVM)
- Evaluation: Accuracy, Classification Report, ROC-AUC
- Exported using `joblib` and loaded dynamically in the app

---

## 🔐 Roles & Access

| Role  | Features |
|-------|----------|
| **User** | Login, make predictions, view suggestions |
| **Admin** | All user privileges + upload new model & scaler |

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit` – frontend
- `scikit-learn` – ML model
- `pandas`, `numpy` – data handling
- `joblib` – model saving/loading

---

## 💡 Retention Strategies

Displayed when churn = **Yes**, based on:
- Age group
- Gender
- Tenure
- Monthly charges

Suggestions are categorized into:
- 💸 Billing & Plan Adjustments
- 🎯 Personalized Offers
- 🤝 Engagement & Support

---

